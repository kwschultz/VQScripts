import sys
sys.path.insert(0,"/home/kasey/Okubo-test/")
import test_plot
reload(test_plot)

import numpy as np
import os
import time


sys.path.insert(0,"/home/kasey/PyVC/")
from pyvc import vcplots
from pyvc import *

# Need to remove a cached file for Arial fonts to be used
if os.path.isfile('/home/kasey/.matplotlib/fontList.cache'):
    os.remove('/home/kasey/.matplotlib/fontList.cache')
#=============================================================================
#        DATA
DTTF        = [1000.0,1000.0,1000.0]   # depth to top of fault (Okubo's style)
_DIP        = [np.pi/2.0,np.pi/3.0,np.pi/6.0]
#_DIP        = [np.pi/5.0,np.pi/10.0,np.pi/4.0]
_L          = [10000.0,10000.0,10000.0]
_W          = [10000.0,10000.0,10000.0]
_C          = [DTTF[i] + _W[i]*np.sin(_DIP[i]) for i in range(len(_L))]   #meters
_US         = [5.0,0.0,0.0]
_UD         = [0.0,-5.0,5.0]
_UT         = [0.0,0.0,0.0]
_LAMBDA     = 3.2e10
_MU         = 3.0e10
#_Xmin,_Xmax = -0.5*_L,1.5*_L  ### Xrange and Yrange must be same
_Xmin,_Xmax = [-90000.0,-90000.0,-90000.0],[100000.0,100000.0,100000.0]
_Nx         = 300.0
#_Ymin,_Ymax = -_W,2*_W
_Ymin,_Ymax = [-95000.0,-90000.0,-90000.0],[95000.0,100000.0,100000.0]
_Ny         = 300.0

##        SWITCHES
#*******************
SAVE         = True
_DG          = False
_DG2         = False
_DZ          = False
_DH          = False
_DIFFG       = False
_DIFFZ       = False
_CLIMITS     = True
_suffix      = '219B'
_HIST        = False
_SHOW        = False
#*******************
"""
sim_file = '../VCModels/ALLCAL2_1-7-11_no-creep/ALLCAL2_1-7-11_no-creep_dyn-0-5_st-5.h5'
evnum    = 10
vcplots.plot_event_field(sim_file, evnum, output_file='test_potential_field_'+str(evnum)+'.png', field_type='potential',
                         fringes=True, padding=0.08, cutoff=None, save_file_prefix=None)
"""

sim_file = '../VCModels/ALLCAL2_1-7-11_no-creep/ALLCAL2_1-7-11_no-creep_dyn-0-5_st-5.h5'
event_range={'type':'year','filter':(0,105)}
output_directory = 'animation_test_v/'
vcplots.event_field_animation(sim_file, output_directory, event_range,
    field_type='potential', fringes=True, padding=0.08, cutoff=None,
    animation_target_length=10.0, animation_fps = 2.0, fade_seconds = 0.5,
    min_mag_marker = 5.0, force_plot=True)





"""
for k in range(len(_C)):
    test_plot.plot_for_cutoff(_Xmin[k],_Xmax[k],_Nx,_Ymin[k],_Ymax[k],_Ny,_C[k],
                        _DIP[k],_L[k],_W[k],_US[k],_UD[k],_UT[k],
                        _LAMBDA,_MU,save=SAVE,SHOW=_SHOW,_CLIMS=_CLIMITS)
"""



"""
#=============================================================================
for k in range(3):
    # Need to remove a cached file for Arial fonts to be used
    if os.path.isfile('/home/kasey/.matplotlib/fontList.cache'):
        os.remove('/home/kasey/.matplotlib/fontList.cache')
    
    test_plot.cbar_plot(_Xmin[k],_Xmax[k],_Nx,_Ymin[k],_Ymax[k],_Ny,_C[k],
                        _DIP[k],_L[k],_W[k],_US[k],_UD[k],_UT[k],
                        _LAMBDA,_MU,save=SAVE,DG2=_DG2,DG=_DG,DZ=_DZ,
                        DH=_DH,DIFFZ=_DIFFZ,DIFFG=_DIFFG,CLIMITS=_CLIMITS,
                        SUFFIX=_suffix,HIST=_HIST,SHOW=_SHOW)

#111111111111111111111111111111111111111111111

center_evnum 	= 109382    #pick a large event to be the centerpiece
duration		= 100 			# in years, make it small for test
sim_file		= 'ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'
with VCSimData() as sim_data:
	sim_data.open_file(sim_file)
	events			= VCEvents(sim_data)
	center_evyear	= events.get_event_year(center_evnum)
start_year	= round(center_evyear)-duration/2.0
end_year	= round(center_evyear)+duration/2.0
#print 'start year: {},end year: {},duration: {}'.format(start_year,end_year,end_year-start_year)
start_time	= time.time()

output_dir  = '../Dropbox/UCD/Stat_Mech_219B/'
tags        = ['mag_area','slip_rupture_length','frequency_mag','recurrence']
output_files= []
for k in range(len(tags)):
    fname = output_dir+tags[k]+'_'+str(duration)+'_ALLCAL2_nocreep.png'
    output_files.append(fname)
    

event_range={'type':'year','filter':(start_year,end_year)}

vcplots.magnitude_rupture_area(sim_file,output_files[0],event_range=event_range)
vcplots.average_slip_surface_rupture_length(sim_file,output_files[1],event_range=event_range)
vcplots.frequency_magnitude(sim_file,output_files[2],event_range=event_range)
#vcplots.plot_recurrence_intervals(sim_file,output_file=output_files[3],event_range=event_range)


print "Total time - {} seconds".format(time.time()-start_time)

"""












