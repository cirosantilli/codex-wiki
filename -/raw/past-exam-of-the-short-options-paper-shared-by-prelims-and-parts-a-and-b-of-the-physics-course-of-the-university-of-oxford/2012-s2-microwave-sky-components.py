"""Original schematic component maps; no measured sky data are reproduced."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white"})
    fig,axes=plt.subplots(1,3,figsize=(14,3.6),subplot_kw={"projection":"mollweide"},layout="constrained")
    lon,lat=np.meshgrid(np.linspace(-np.pi,np.pi,361),np.linspace(-np.pi/2,np.pi/2,181))
    dust=np.exp(-.5*(lat/.13)**2)*(1+.3*np.cos(3*lon)+.2*np.sin(7*lon))
    dipole=2.725*.00105*1000*(np.cos(lat)*np.cos(lon)*np.cos(.6)+np.sin(lat)*np.sin(.6))
    patch=(np.sin(7*lon+2*np.sin(lat))*np.cos(3*lat)+.6*np.cos(13*lon-3*lat)+.4*np.sin(19*lon+7*lat))*np.cos(lat)**2
    patch=27*patch/np.sqrt(np.average(patch**2,weights=np.cos(lat)))
    for ax,data,title,cmap,label in zip(axes,[dust,dipole,patch],["Galactic dust foreground","Motion-induced dipole","Intrinsic anisotropy (toy pattern)"],["inferno","coolwarm","coolwarm"],["relative dust intensity",r"$\Delta T$ [mK]",r"illustrative $\Delta T$ [$\mu$K]"]):
        v={}if cmap=="inferno"else dict(vmin=-np.max(abs(data)),vmax=np.max(abs(data)))
        im=ax.pcolormesh(lon,lat,data,cmap=cmap,rasterized=True,shading="auto",**v);ax.grid(alpha=.25);ax.set_title(title,fontsize=12);ax.tick_params(labelsize=8)
        cb=fig.colorbar(im,ax=ax,orientation="horizontal",shrink=.85,pad=.07);cb.set_label(label,fontsize=9);cb.ax.tick_params(labelsize=8)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white");plt.close(fig)


if __name__=="__main__":main()
