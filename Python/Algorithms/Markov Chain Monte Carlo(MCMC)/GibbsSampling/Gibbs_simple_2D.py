import numpy as np
import matplotlib.pyplot as plt

# Gibbs 샘플링에 사용할 2차원 정규분포의 설정
mu_1, mu_2 = 0, 0  # 두 변수의 평균
sigma_1, sigma_2 = 1, 1  # 두 변수의 표준편차
rho = 0.8  # 두 변수 사이의 상관관계 (covariance)

# 조건부 분포 함수 (조건부 분포는 1차원 정규분포)
def sample_x1_given_x2(x2, mu_1, mu_2, sigma_1, sigma_2, rho):
    cond_mean = mu_1 + rho * (sigma_1 / sigma_2) * (x2 - mu_2)
    cond_std = np.sqrt((1 - rho**2) * sigma_1**2)
    return np.random.normal(cond_mean, cond_std)

def sample_x2_given_x1(x1, mu_1, mu_2, sigma_1, sigma_2, rho):
    cond_mean = mu_2 + rho * (sigma_2 / sigma_1) * (x1 - mu_1)
    cond_std = np.sqrt((1 - rho**2) * sigma_2**2)
    return np.random.normal(cond_mean, cond_std)

# Gibbs 샘플링 함수
def gibbs_sampling(num_samples, initial_values, mu_1, mu_2, sigma_1, sigma_2, rho):
    x1_samples = [initial_values[0]]
    x2_samples = [initial_values[1]]
    
    for _ in range(num_samples):
        # X1을 X2에 조건부로 샘플링
        x1_new = sample_x1_given_x2(x2_samples[-1], mu_1, mu_2, sigma_1, sigma_2, rho)
        x1_samples.append(x1_new)
        
        # X2를 X1에 조건부로 샘플링
        x2_new = sample_x2_given_x1(x1_samples[-1], mu_1, mu_2, sigma_1, sigma_2, rho)
        x2_samples.append(x2_new)
    
    return np.array(x1_samples), np.array(x2_samples)

# 초기값 및 샘플 개수 설정
initial_values = [0, 0]  # X1, X2의 초기값
num_samples = 10000  # 샘플 수

# Gibbs 샘플링 실행
x1_samples, x2_samples = gibbs_sampling(num_samples, initial_values, mu_1, mu_2, sigma_1, sigma_2, rho)

# 샘플링된 결과 시각화
plt.figure(figsize=(10, 6))
plt.scatter(x1_samples, x2_samples, alpha=0.3, s=2)
plt.title('Gibbs Sampling from Bivariate Normal Distribution')
plt.xlabel('X1')
plt.ylabel('X2')
plt.grid(True)
plt.show()
