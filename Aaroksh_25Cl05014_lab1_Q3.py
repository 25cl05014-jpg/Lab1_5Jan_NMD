# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 17:59:16 2026

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

djf = [12,1,2]
mam = [3,4,5]
jjas = [6,7,8,9]
on = [10,11]

sst1_djf = temp.sel(time = temp['time.month'].isin(djf),latitude=8.0).mean(dim='time')
sst1_mam = temp.sel(time = temp['time.month'].isin(mam),latitude=8.0).mean(dim='time')
sst1_jjas = temp.sel(time = temp['time.month'].isin(jjas),latitude=8.0).mean(dim='time')
sst1_on = temp.sel(time = temp['time.month'].isin(on),latitude=8.0).mean(dim='time')


sst2_djf = temp.sel(time = temp['time.month'].isin(djf),latitude=12.0).mean(dim='time')
sst2_mam= temp.sel(time = temp['time.month'].isin(mam),latitude=12.0).mean(dim='time')
sst2_jjas = temp.sel(time = temp['time.month'].isin(jjas),latitude=12.0).mean(dim='time')
sst2_on = temp.sel(time = temp['time.month'].isin(on),latitude=12.0).mean(dim='time')


sst3_djf = temp.sel(time = temp['time.month'].isin(djf),latitude=15.0).mean(dim='time')
sst3_mam = temp.sel(time = temp['time.month'].isin(mam),latitude=15.0).mean(dim='time')
sst3_jjas = temp.sel(time = temp['time.month'].isin(jjas),latitude=15.0).mean(dim='time')
sst3_on = temp.sel(time = temp['time.month'].isin(on),latitude=15.0).mean(dim='time')


sst4_djf = temp.sel(time = temp['time.month'].isin(djf),latitude=18.0).mean(dim='time')
sst4_mam = temp.sel(time = temp['time.month'].isin(mam),latitude=18.0).mean(dim='time')
sst4_jjas = temp.sel(time = temp['time.month'].isin(jjas),latitude=18.0).mean(dim='time')
sst4_on= temp.sel(time = temp['time.month'].isin(on),latitude=18.0).mean(dim='time')


plt.figure(figsize = (25,15))
plt.suptitle("Temperature depth profile for different seasons at different latitudes",fontsize = 28)



plt.subplot(2,2,1)
plt.plot(sst1_djf.values,ds["depth"].values,color = "Blue",label = "DJF")
plt.plot(sst1_mam.values,ds["depth"].values,color = "Red",label = "MAM")
plt.plot(sst1_jjas.values,ds["depth"].values,color = "Orange",label = "JJAS")
plt.plot(sst1_on.values,ds["depth"].values,color = "Green",label = "ON")
plt.ylim(0,200)
plt.gca().invert_yaxis()
plt.legend(loc="upper left")
plt.title("Seasonal Temperature depth profile at 8$^\circ$N",fontsize = 20)
plt.xlabel("Temperature",fontsize = 15)
plt.ylabel("Depth[m]",fontsize = 15)
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(sst2_djf.values,ds["depth"].values,color = "Blue",label = "DJF")
plt.plot(sst2_mam.values,ds["depth"].values,color = "Red",label = "MAM")
plt.plot(sst2_jjas.values,ds["depth"].values,color = "Orange",label = "JJAS")
plt.plot(sst2_on.values,ds["depth"].values,color = "Green",label = "ON")
plt.ylim(0,200)
plt.gca().invert_yaxis()
plt.legend(loc="upper left")
plt.title("Seasonal Temperature depth profile at 12$^\circ$N",fontsize = 20)
plt.xlabel("Temperature",fontsize = 15)
plt.ylabel("Depth[m]",fontsize = 15)
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(sst3_djf.values,ds["depth"].values,color = "Blue",label = "DJF")
plt.plot(sst3_mam.values,ds["depth"].values,color = "Red",label = "MAM")
plt.plot(sst3_jjas.values,ds["depth"].values,color = "Orange",label = "JJAS")
plt.plot(sst3_on.values,ds["depth"].values,color = "Green",label = "ON")
plt.ylim(0,200)
plt.gca().invert_yaxis()
plt.legend(loc="upper left")
plt.title("Seasonal Temperature depth profile at 15$^\circ$N",fontsize = 20)
plt.xlabel("Temperature",fontsize = 15)
plt.ylabel("Depth[m]",fontsize = 15)
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(sst4_djf.values,ds["depth"].values,color = "Blue",label = "DJF")
plt.plot(sst4_mam.values,ds["depth"].values,color = "Red",label = "MAM")
plt.plot(sst4_jjas.values,ds["depth"].values,color = "Orange",label = "JJAS")
plt.plot(sst4_on.values,ds["depth"].values,color = "Green",label = "ON")
plt.ylim(0,200)
plt.gca().invert_yaxis()
plt.legend(loc="upper left")
plt.title("Seasonal Temperature depth profile at 18$^\circ$N",fontsize = 20)
plt.xlabel("Temperature",fontsize = 15)
plt.ylabel("Depth[m]",fontsize = 15)
plt.grid(True)


'''
sst1_djf = temp.sel(time = temp['time.month'].isin(djf),latitude=8.0).mean(dim='time')
plt.plot(sst1_djf.values,ds["depth"].values,color = "Blue",label = "DJF")
plt.ylim(0,200)
'''
sss1_djf = salin.sel(time = temp['time.month'].isin(djf),latitude=8.0).mean(dim='time')
sss1_mam = salin.sel(time = temp['time.month'].isin(mam),latitude=8.0).mean(dim='time')
sss1_jjas = salin.sel(time = temp['time.month'].isin(jjas),latitude=8.0).mean(dim='time')
sss1_on = salin.sel(time = temp['time.month'].isin(on),latitude=8.0).mean(dim='time')

sss2_djf = salin.sel(time = temp['time.month'].isin(djf),latitude=12.0).mean(dim='time')
sss2_mam = salin.sel(time = temp['time.month'].isin(mam),latitude=12.0).mean(dim='time')
sss2_jjas = salin.sel(time = temp['time.month'].isin(jjas),latitude=12.0).mean(dim='time')
sss2_on = salin.sel(time = temp['time.month'].isin(on),latitude=12.0).mean(dim='time')

sss3_djf = salin.sel(time = temp['time.month'].isin(djf),latitude=15.0).mean(dim='time')
sss3_mam = salin.sel(time = temp['time.month'].isin(mam),latitude=15.0).mean(dim='time')
sss3_jjas = salin.sel(time = temp['time.month'].isin(jjas),latitude=15.0).mean(dim='time')
sss3_on = salin.sel(time = temp['time.month'].isin(on),latitude=15.0).mean(dim='time')


sss4_djf = salin.sel(time = temp['time.month'].isin(djf),latitude=18.0).mean(dim='time')
sss4_mam = salin.sel(time = temp['time.month'].isin(mam),latitude=18.0).mean(dim='time')
sss4_jjas = salin.sel(time = temp['time.month'].isin(jjas),latitude=18.0).mean(dim='time')
sss4_on = salin.sel(time = temp['time.month'].isin(on),latitude=18.0).mean(dim='time')



plt.figure(figsize = (25,15))
plt.suptitle("Salinity depth profile for different seasons at different latitudes",fontsize = 28)



plt.subplot(2,2,1)
plt.plot(sss1_djf.values,ds["depth"].values,color = "Blue",label = "DJF")
plt.plot(sss1_mam.values,ds["depth"].values,color = "Red",label = "MAM")
plt.plot(sss1_jjas.values,ds["depth"].values,color = "Orange",label = "JJAS")
plt.plot(sss1_on.values,ds["depth"].values,color = "Green",label = "ON")
plt.ylim(0,200)
plt.gca().invert_yaxis()
plt.legend(loc="upper right")
plt.title("Seasonal Salinity depth profile at 8$^\circ$N",fontsize = 20)
plt.xlabel("Temperature",fontsize = 15)
plt.ylabel("Depth[m]",fontsize = 15)
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(sss2_djf.values,ds["depth"].values,color = "Blue",label = "DJF")
plt.plot(sss2_mam.values,ds["depth"].values,color = "Red",label = "MAM")
plt.plot(sss2_jjas.values,ds["depth"].values,color = "Orange",label = "JJAS")
plt.plot(sss2_on.values,ds["depth"].values,color = "Green",label = "ON")
plt.ylim(0,200)
plt.gca().invert_yaxis()
plt.legend(loc="upper right")
plt.title("Seasonal Salinity depth profile at 12$^\circ$N",fontsize = 20)
plt.xlabel("Temperature",fontsize = 15)
plt.ylabel("Depth[m]",fontsize = 15)
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(sss3_djf.values,ds["depth"].values,color = "Blue",label = "DJF")
plt.plot(sss3_mam.values,ds["depth"].values,color = "Red",label = "MAM")
plt.plot(sss3_jjas.values,ds["depth"].values,color = "Orange",label = "JJAS")
plt.plot(sss3_on.values,ds["depth"].values,color = "Green",label = "ON")
plt.ylim(0,200)
plt.gca().invert_yaxis()
plt.legend(loc="upper right")
plt.title("Seasonal Salinity depth profile at 15$^\circ$N",fontsize = 20)
plt.xlabel("Temperature",fontsize = 15)
plt.ylabel("Depth[m]",fontsize = 15)
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(sss4_djf.values,ds["depth"].values,color = "Blue",label = "DJF")
plt.plot(sss4_mam.values,ds["depth"].values,color = "Red",label = "MAM")
plt.plot(sss4_jjas.values,ds["depth"].values,color = "Orange",label = "JJAS")
plt.plot(sss4_on.values,ds["depth"].values,color = "Green",label = "ON")
plt.ylim(0,200)
plt.gca().invert_yaxis()
plt.legend(loc="upper right")
plt.title("Seasonal Salinity depth profile at 18$^\circ$N",fontsize = 20)
plt.xlabel("Temperature",fontsize = 15)
plt.ylabel("Depth[m]",fontsize = 15)
plt.grid(True)

