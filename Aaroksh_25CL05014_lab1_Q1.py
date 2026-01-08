# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 18:15:31 2026

@author: user
"""

import xarray as xr

data = "C:/Users/user/Desktop/25CL05014-NMD/mvl_lab_5jan_mtech.nc"
ds = xr.open_dataset(data)
print(ds)

ds.data_vars

temp = ds['thetao_oras']
salin = ds['so_oras']

import matplotlib.pyplot as plt
import numpy as np

#For creating a time series for sea surface temperature over 8 degrees N latitude
reg_sst1 = temp.sel(latitude = 8.0,depth = slice(0.5058))
reg_sst1.plot(color = 'Blue')
plt.xlabel('Time')
plt.ylabel('SST')
plt.title("Time series plot of Sea surface temperature over 8 degrees N")
plt.grid(True)

#For creating a time series for sea surface temperature over 12 degrees N latitude
reg_sst2 = temp.sel(latitude = 12.0,depth = slice(0.5058))
reg_sst2.plot()
plt.xlabel('Time')
plt.ylabel('SST')
plt.title("Time series plot of Sea surface temperature over 12 degrees N")
plt.grid(True)

#For creating a time series for sea surface temperature over 15 degrees N latitude
reg_sst3 = temp.sel(latitude = 15.0,depth = slice(0.5058))
reg_sst3.plot(color = 'Red')
plt.xlabel('Time')
plt.ylabel('SST')
plt.title("Time series plot of Sea surface temperature over 15 degrees N")
plt.grid(True)

#For creating a time series for sea surface temperature over 18 degrees N latitude
reg_sst4 = temp.sel(latitude = 18.0,depth = slice(0.5058))
reg_sst4.plot(color = 'Orange')
plt.xlabel('Time')
plt.ylabel('SST')
plt.title("Time series plot of Sea surface temperature over 18 degrees N")
plt.grid(True)

#For creating a time series for sea surface salinity over 8 degrees N latitude
reg_sss1 = salin.sel(latitude = 8.0,depth = slice(0.5058))
reg_sss1.plot()
plt.title("Time series plot of Sea surface Salinity over 8 degrees N")
plt.xlabel('Time')
plt.ylabel('Sea surface Salinity')
plt.grid(True)

#For creating a time series for sea surface salinity over 12 degrees N latitude
reg_sss2 = salin.sel(latitude = 12.0,depth = slice(0.5058))
reg_sss2.plot(color = 'Purple')
plt.title("Time series plot of Sea surface Salinity over 12 degrees N")
plt.xlabel('Time')
plt.ylabel('Sea surface Salinity')
plt.grid(True)

#For creating a time series for sea surface salinity over 15 degrees N latitude
reg_sss3 = salin.sel(latitude = 15.0,depth = slice(0.5058))
reg_sss3.plot(color = 'Maroon')
plt.title("Time series plot of Sea surface Salinity over 15 degrees N")
plt.xlabel('Time')
plt.ylabel('Sea surface Salinity')
plt.grid(True)

#For creating a time series for sea surface salinity over 18 degrees N latitude
reg_sss4 = salin.sel(latitude = 18.0,depth = slice(0.5058))
reg_sss4.plot(color = 'Orange')
plt.title("Time series plot of Sea surface Salinity over 18 degrees N")
plt.xlabel('Time')
plt.ylabel('Sea surface Salinity')
plt.grid(True)
