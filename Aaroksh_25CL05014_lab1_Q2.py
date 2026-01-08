# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 18:08:52 2026

@author: user
"""

import xarray as xr
data = "C:/Users/user/Desktop/25CL05014-NMD/mvl_lab_5jan_mtech.nc"
ds = xr.open_dataset(data)
print(ds)

ds.data_vars

temp = ds['thetao_oras']
salin = ds['so_oras']
depth = ds['depth']
time = ds['time']

import matplotlib.pyplot as plt
import numpy as np

# For creating time depth section at given latitudes upto 100m depth

# Extracting the sst data for the different latitudes
reg_sst1 = temp.sel(latitude=8.0, time=slice('2000-01-01','2020-12-31'), depth=slice(0,100)).mean(dim='longitude')
reg_sst2 = temp.sel(latitude=12.0, time=slice('2000-01-01','2020-12-31'), depth=slice(0,100)).mean(dim='longitude')
reg_sst3 = temp.sel(latitude=15.0, time=slice('2000-01-01','2020-12-31'), depth=slice(0,100)).mean(dim='longitude')
reg_sst4 = temp.sel(latitude=18.0, time=slice('2000-01-01','2020-12-31'), depth=slice(0,100)).mean(dim='longitude')

# Creating subplots
plt.figure(figsize = (25,15))
plt.suptitle("Time depth section of temperature at given latitudes upto 100m depth",fontsize = 22)


plt.subplot(2,2,1)
reg_sst1.plot(x= "time", y = "depth")
plt.gca().invert_yaxis()
plt.title("8$^\circ$N Latitude",fontsize = 15)

plt.subplot(2,2,2)
reg_sst2.plot(x= "time", y = "depth")
plt.gca().invert_yaxis()
plt.title("12$^\circ$N Latitude",fontsize = 15)

plt.subplot(2,2,3)
reg_sst3.plot(x= "time", y = "depth")
plt.gca().invert_yaxis()
plt.title("15$^\circ$N Latitude",fontsize = 15)

plt.subplot(2,2,4)
reg_sst4.plot(x= "time", y = "depth")
plt.gca().invert_yaxis()
plt.title("18$^\circ$N Latitude",fontsize = 15)

#Extracting the sss data for different latitudes

reg_sss1 = salin.sel(latitude=8.0, time=slice('2000-01-01','2020-12-31'), depth=slice(0,100)).mean(dim='longitude')
reg_sss2 = salin.sel(latitude=12.0, time=slice('2000-01-01','2020-12-31'), depth=slice(0,100)).mean(dim='longitude')
reg_sss3 = salin.sel(latitude=15.0, time=slice('2000-01-01','2020-12-31'), depth=slice(0,100)).mean(dim='longitude')
reg_sss4 = salin.sel(latitude=18.0, time=slice('2000-01-01','2020-12-31'), depth=slice(0,100)).mean(dim='longitude')

plt.figure(figsize = (25,15))
plt.suptitle("Time depth section of salinity at given latitudes upto 100m depth",fontsize = 22)

plt.subplot(2,2,1)
reg_sss1.plot(x= "time", y = "depth")
plt.gca().invert_yaxis()
plt.title("8$^\circ$N Latitude",fontsize = 15)

plt.subplot(2,2,2)
reg_sss2.plot(x= "time", y = "depth")
plt.gca().invert_yaxis()
plt.title("12$^\circ$N Latitude",fontsize = 15)

plt.subplot(2,2,3)
reg_sss3.plot(x= "time", y = "depth")
plt.gca().invert_yaxis()
plt.title("15$^\circ$N Latitude",fontsize = 15)

plt.subplot(2,2,4)
reg_sss4.plot(x= "time", y = "depth")
plt.gca().invert_yaxis()
plt.title("18$^\circ$N Latitude",fontsize = 15)


