import numpy as np
import matplotlib.pyplot as plt

def gibbs_sampling_3d(mu, sigma, num_samples):
    # 샘플을 저장할 배열
    samples = np.zeros((num_samples, 3))

    # 초기값 설정
    x1, x2, x3 = 0, 0, 0

    # 샘플링 과정
    for i in range(num_samples):
        # 3차원 정규분포의 조건부 분포를 샘플링
        # 조건부 평균과 분산 계산
        # X2와 X3에 조건부로 X1 샘플링
        cond_mean1 = mu[0] + sigma[0, 1] * (x2 - mu[1]) / sigma[1, 1] + sigma[0, 2] * (x3 - mu[2]) / sigma[2, 2]
        cond_std1 = np.sqrt(sigma[0, 0] - (sigma[0, 1]**2 / sigma[1, 1]) - (sigma[0, 2]**2 / sigma[2, 2]))

        # 오버플로우 방지를 위해 값을 제한
        cond_mean1 = np.clip(cond_mean1, -1e10, 1e10)
        cond_std1 = np.clip(cond_std1, 1e-10, 1e10)

        x1 = np.random.normal(cond_mean1, cond_std1)

        # X1과 X3에 조건부로 X2 샘플링
        cond_mean2 = mu[1] + sigma[1, 0] * (x1 - mu[0]) / sigma[0, 0] + sigma[1, 2] * (x3 - mu[2]) / sigma[2, 2]
        cond_std2 = np.sqrt(sigma[1, 1] - (sigma[1, 0]**2 / sigma[0, 0]) - (sigma[1, 2]**2 / sigma[2, 2]))

        cond_mean2 = np.clip(cond_mean2, -1e10, 1e10)
        cond_std2 = np.clip(cond_std2, 1e-10, 1e10)

        x2 = np.random.normal(cond_mean2, cond_std2)
        
        # X1과 X2에 조건부로 X3 샘플링
        cond_mean3 = mu[2] + sigma[2, 0] * (x1 - mu[0]) / sigma[0, 0] + sigma[2, 1] * (x2 - mu[1]) / sigma[1, 1]
        cond_std3 = np.sqrt(sigma[2, 2] - (sigma[2, 0]**2 / sigma[0, 0]) - (sigma[2, 1]**2 / sigma[1, 1]))

        cond_mean3 = np.clip(cond_mean3, -1e10, 1e10)
        cond_std3 = np.clip(cond_std3, 1e-10, 1e10)

        x3 = np.random.normal(cond_mean3, cond_std3)

        samples[i] = [x1, x2, x3]

    return samples

# 공분산 행렬과 평균 설정
# 3차원 정규분포의 평균과 공분산 행렬
mu = np.array([0, 0, 0])
sigma = np.array([[1, 0.5, 0.3],
                  [0.5, 1, 0.4],
                  [0.3, 0.4, 1]])

# 초기값 및 샘플 개수 설정
# 샘플링 개수
num_samples = 1000

# Gibbs 샘플링 실행
samples = gibbs_sampling_3d(mu, sigma, num_samples)

# 샘플링된 결과를 3D 산점도로 시각화
# 결과를 3D 그래프로 시각화
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(samples[:, 0], samples[:, 1], samples[:, 2], s=1)
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('X3')

plt.show()
