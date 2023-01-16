from ast import Str
import math
import struct
import wave
import sys

def sinewave(limit: int, a: int, omega: float):
    """正弦波样本生成器。
    limit 指定生成的总样本数
    a 指定振幅大小
    omega 指定角转速
    """
    for n in range(limit):
        yield int(a*math.sin(omega*n))
def generateSineWaveFile(file: Str, sampleRate: int, frequency: int, duration: float):
    """生成一个特定正弦波的音频文件。
    file 指定文件名
    sampleRate 指定采样频率（单位：赫兹）
    frequency 指定频率（单位： 赫兹）
    duration 指定时常（单位：秒）
    """
    # 补全文件名
    if file.casefold()[-4:] != ".wav":file += '.wav'
    # 振幅。
    amplitude = 10000
    # 每周期样本数。
    samplesPerCycle = sampleRate // frequency
    # 总样本数。
    totalSamples = int(duration*sampleRate)
    # 使最后一次的样本值与第一次样本值相同，都为 0，因此需要保证 totalSamples 是 samplesPerCycle 的倍数 + 1。
    if rem := totalSamples % samplesPerCycle:
        totalSamples = totalSamples+(samplesPerCycle - rem)
        totalSamples = totalSamples+1
    # 创建波形文件并循环写入采样数据。
    
    with wave.open(file, 'wb') as wf:
        # 设置为单声道。
        wf.setnchannels(1)
        # 设置采样量化位数为双字节16位。
        wf.setsampwidth(2)
        # 设置采样率。
        wf.setframerate(sampleRate)
        # 样本间隔角旋转量。
        omega = 2*math.pi/(sampleRate/frequency)
        # 遍历每一个采样点。
        for s in sinewave(totalSamples, amplitude, omega):
            # 将采样数据打包成字节数据写入波形文件。
            data = struct.pack('<h', int(s))
            wf.writeframes(data)
def main():
    try:
        if len(sys.argv) < 4:
            filename = f"{sys.argv[1]}Hz_{sys.argv[2]}s.wav"
            generateSineWaveFile(filename, 48000, int(sys.argv[1]), float(sys.argv[2]))
        else:generateSineWaveFile(sys.argv[1], 48000, int(sys.argv[2]), float(sys.argv[3]))
    except IndexError:
        print('简易波形生成器')
        filename = input('请输入用于保存波形的文件名： ')
        frequency = input('正弦波的声音频率（单位：赫兹）：')
        duration = input('持续时间（单位：秒）： ')
        if filename == '':filename = f"{frequency}Hz_{duration}s.wav"
        generateSineWaveFile(filename, 48000, int(frequency), float(duration))

if __name__ == "__main__":
    main()