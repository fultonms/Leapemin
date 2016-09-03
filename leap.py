import sys, math, pyaudio, time
sys.path.insert(0, "/usr/src/LeapSDK/lib/")
sys.path.insert(0, "/usr/src/LeapSDK/lib/x64/")
import Leap

bitrate = 16000
controller = Leap.Controller()

controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)
controller.set_policy(Leap.Controller.POLICY_IMAGES)
controller.set_policy(Leap.Controller.POLICY_OPTIMIZE_HMD)

PyAudio = pyaudio.PyAudio
p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = bitrate, 
                output = True)
exit = False
length = 0.05
while not exit:
	frame = controller.frame()
	hand = frame.hands[0]
	freq = hand.palm_position.y * 35/4
	print freq
	numOfFrames = int(bitrate * length)
	restFrames = numOfFrames % bitrate
	waveData = ''
	if freq != 0:
		for x in xrange(numOfFrames):
			waveData = waveData + chr(int(math.sin(x/((bitrate/freq)/math.pi))*127+128))
		for x in xrange(restFrames):
	       		waveData = waveData+chr(128)
	stream.write(waveData)

stream.stop_stream()
stream.close()
p.terminate()


