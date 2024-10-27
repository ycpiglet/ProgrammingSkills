import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 목표 분포: 1차원 정규분포 (평균 0, 표준편차 1)
def target_distribution(x):
    return np.exp(-0.5 * x**2)

# MH 알고리즘 (수락/거부 과정 시각화를 위해 수정된 버전)
def metropolis_hastings(target_dist, proposal_dist, num_samples, init_sample):
    samples = [init_sample]
    current_sample = init_sample

    proposed_samples = []
    acceptance_ratios = []
    random_samples = []
    accepted = []

    for i in range(num_samples):
        proposed_sample = proposal_dist(current_sample)
        proposed_samples.append(proposed_sample)

        # 목표 분포 비율 (수락 확률 계산)
        acceptance_ratio = min(1, target_dist(proposed_sample) / target_dist(current_sample))
        acceptance_ratios.append(acceptance_ratio)

        # 랜덤 샘플 (0과 1 사이에서 샘플링)
        random_sample = np.random.rand()
        random_samples.append(random_sample)

        # 수락 여부 결정
        if random_sample < acceptance_ratio:
            current_sample = proposed_sample
            accepted.append(True)
        else:
            accepted.append(False)

        samples.append(current_sample)
    
    return np.array(samples), proposed_samples, acceptance_ratios, random_samples, accepted

# 제안 분포: 정규 분포에서 샘플링 (평균 현재 상태, 표준편차 1)
def proposal_distribution(x):
    return np.random.normal(x, 1.0)

# 초기 샘플, 총 샘플 수 설정
initial_sample = 0
num_samples = 500

# Metropolis-Hastings 알고리즘 실행
samples, proposed_samples, acceptance_ratios, random_samples, accepted = metropolis_hastings(
    target_distribution, proposal_distribution, num_samples, initial_sample
)

# 시각화를 위한 설정
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(-4, 4, 100)
ax.plot(x, np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi), 'r-', lw=2, label='Target Distribution')
ax.set_ylim(0, 0.5)
ax.set_xlim(-5, 5)

# 현재 샘플, 제안된 샘플, 수락 여부 시각화용 점
current_sample_dot, = ax.plot([], [], 'bo', label='Current Sample')
proposed_sample_dot, = ax.plot([], [], 'go', label='Proposed Sample')
accepted_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12, color='black')

# 애니메이션 업데이트 함수
def update(frame):
    # 현재 상태를 초기화
    current_sample_dot.set_data(samples[frame], target_distribution(samples[frame]))
    proposed_sample_dot.set_data(proposed_samples[frame], target_distribution(proposed_samples[frame]))

    # 수락 여부 표시
    if accepted[frame]:
        accepted_text.set_text(f'Accepted: Yes (Acc. Ratio: {acceptance_ratios[frame]:.3f}, Rand: {random_samples[frame]:.3f})')
        accepted_text.set_color('green')
    else:
        accepted_text.set_text(f'Accepted: No (Acc. Ratio: {acceptance_ratios[frame]:.3f}, Rand: {random_samples[frame]:.3f})')
        accepted_text.set_color('red')
    
    return current_sample_dot, proposed_sample_dot, accepted_text

# 애니메이션 설정
ani = FuncAnimation(fig, update, frames=range(num_samples), repeat=False)

plt.legend()
plt.show()
