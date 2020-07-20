import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1) # 0부터 6까지 0.1 간격으로 생성
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1, label="sin")
plt.plot(x,y2, label="cos", linestyle="--", color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend() # label 명을 보여주는 함수
plt.show()
