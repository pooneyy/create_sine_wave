# Create Sine Wave

Create a sine wave file using python.

使用Python创建一个正弦波形文件。

#### 使用方法

创建一个文件名为`1kHz.1s.wav`、频率为`1kHz`、时长`1`秒的波形文件

- 示例1，在文件名后附加参数：

  ```sh
  python sineWave.py 1kHz.wav 1000 1
  ```

- 示例2，当你在文件名后附加的参数未包含文件名时，会为你补全文件名：

  ```
  python sineWave.py 1000 1
  ```

- 示例3，亦可直接运行，根据提示输入参数，文件名可不填：

  ```sh
  >sineWave.py
  简易波形生成器
  请输入用于保存波形的文件名：
  正弦波的声音频率（单位：赫兹）：500
  持续时间（单位：秒）： 5
  ```

  

[用 Python 简单生成 WAV 波形声音文件 (张赐荣@bbsmax.com)](https://www.bbsmax.com/A/qVdeoKNbJP/)