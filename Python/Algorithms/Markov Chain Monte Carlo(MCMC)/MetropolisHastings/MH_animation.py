import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 목표 분포: 1차원 정규분포 (평균 0, 표준편차 1)
def target_distribution(x):
    return np.exp(-0.5 * x**2)

# MH 알고리즘
def metropolis_hastings(target_dist, proposal_dist, num_samples, init_sample):
    samples = [init_sample]
    current_sample = init_sample

    for i in range(num_samples):
        proposed_sample = proposal_dist(current_sample)
        acceptance_ratio = target_dist(proposed_sample) / target_dist(current_sample)
        
        if np.random.rand() < acceptance_ratio:
            current_sample = proposed_sample

        samples.append(current_sample)
    
    return np.array(samples)

# 제안 분포: 정규 분포에서 샘플링 (평균 현재 상태, 표준편차 1)
def proposal_distribution(x):
    return np.random.normal(x, 1.0)

# 초기 샘플, 총 샘플 수 설정
initial_sample = 0
num_samples = 20000

# Metropolis-Hastings 알고리즘 실행
samples = metropolis_hastings(target_distribution, proposal_distribution, num_samples, initial_sample)

# 시각화를 위한 설정
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(-4, 4, 100)
ax.plot(x, np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi), 'r-', lw=2, label='Target Distribution')
hist_data, bins, _ = ax.hist([], bins=50, density=True, alpha=0.6, color='b', label='MH Samples')
ax.legend()

# 애니메이션 업데이트 함수
def update(frame):
    ax.cla()  # 이전 상태 초기화
    ax.plot(x, np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi), 'r-', lw=2, label='Target Distribution')
    ax.hist(samples[:frame], bins=50, density=True, alpha=0.6, color='b', label='MH Samples')
    ax.legend()
    ax.set_title(f'Iteration {frame}')
    
# 애니메이션 설정
ani = FuncAnimation(fig, update, frames=range(0, num_samples, 100), repeat=False)

plt.show()
