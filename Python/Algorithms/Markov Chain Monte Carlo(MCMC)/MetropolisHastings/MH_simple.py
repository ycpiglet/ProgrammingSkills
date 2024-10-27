import numpy as np
import matplotlib.pyplot as plt

# 목표 분포: 1차원 정규분포 (평균 0, 표준편차 1)
def target_distribution(x):
    return np.exp(-0.5 * x**2)

# MH 알고리즘
def metropolis_hastings(target_dist, proposal_dist, num_samples, init_sample):
    samples = [init_sample]  # 샘플을 저장할 리스트
    current_sample = init_sample

    for i in range(num_samples):
        # 제안된 샘플 생성
        proposed_sample = proposal_dist(current_sample)
        
        # 목표 분포에서의 비율 (수락 확률 계산)
        acceptance_ratio = target_dist(proposed_sample) / target_dist(current_sample)
        
        # 수락 여부 결정
        if np.random.rand() < acceptance_ratio:
            current_sample = proposed_sample  # 수락되면 제안된 샘플을 현재 샘플로

        samples.append(current_sample)  # 현재 샘플 저장
    
    return np.array(samples)

# 제안 분포: 정규 분포에서 샘플링 (평균 현재 상태, 표준편차 1)
def proposal_distribution(x):
    return np.random.normal(x, 1.0)

# 초기 샘플, 총 샘플 수 설정
initial_sample = 0
num_samples = 10000

# Metropolis-Hastings 알고리즘 실행
samples = metropolis_hastings(target_distribution, proposal_distribution, num_samples, initial_sample)

# 결과 시각화
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=50, density=True, alpha=0.6, color='b', label='MH Samples')
x = np.linspace(-4, 4, 100)
plt.plot(x, np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi), 'r-', lw=2, label='Target Distribution')
plt.title('Metropolis-Hastings Sampling from Normal Distribution')
plt.legend()
plt.show()
