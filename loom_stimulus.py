from psychopy import visual, core, monitors

#stimulus parameters
start_size = 1.4 #deg
end_size = 14 #deg

diff_size = end_size - start_size #by how much we have to increase radius

#frame rate is 60 Hz
frame_rate = 60
IFI = 1 / 60 #time bw each flip

expand_time_s = 250 / 1000
num_frames_expand = int(expand_time_s * frame_rate)
inc_per_frame = diff_size / num_frames_expand #degrees per frame

hold_time_s = 250 / 1000
num_frames_hold = int(hold_time_s * frame_rate)

pause_time_s = 1 - (expand_time_s + hold_time_s)
num_frames_pause = int(frame_rate - (num_frames_expand + num_frames_hold))

no_repeats = 15



screen_no = 0
screen_dimensions = [1500, 1000] #need to check later

#make the window
mywin = visual.Window(size=screen_dimensions, screen=screen_no, monitor = 'testmonitor',
                      color=(0,0,0), fullscr=True, units='deg')

#make the circle
circ_stim = visual.Circle(win=mywin, radius=start_size, units='deg',
                          fillColor=[-1, -1, -1], lineColor=[-1,-1,-1], edges=128)

circ_stim.draw() #will draw the circle stimulus onto window


#loop program
for i in range(no_repeats):
    for j in range(num_frames_expand):
        circ_stim.radius=start_size + (j * inc_per_frame)
        circ_stim.draw()
        mywin.flip()

    for j in range(num_frames_hold):
        circ_stim.radius = end_size #degrees
        circ_stim.draw()
        mywin.flip()

    for j in range(num_frames_pause):
        circ_stim.radius=0
        circ_stim.draw()
        mywin.flip()

mywin.close()
