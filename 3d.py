from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np



def plotHist2D(mrange):
    sampleData=np.loadtxt("data/v3/"+f+"_sample100000.gz")
    maxSNR=max(sampleData[:,0])
    minSNR=8
    maxMz=max(sampleData[:,4])
    minMz=1
    binsSNR=200
    binsMz=200
#    xedges = np.linspace(minSNR,maxSNR,binsSNR)
#    yedges = np.linspace(minMz,maxMz,binsMz)
    xedges=np.logspace(start=np.log10(minSNR),stop=np.log10(maxSNR),num=binsSNR)
    yedges=np.logspace(start=np.log10(minMz),stop=np.log10(maxMz),num=binsMz)
    x=sampleData[:,0]
    y=sampleData[:,4]
    fig = plt.figure(figsize=(7, 3))
    H, xedges, yedges = np.histogram2d(x, y, bins=(xedges, yedges))
    H = H.T  # Let each row list bins with common y range.
    ax = fig.add_subplot(111, title=f)
    plt.xlabel('SNR')
    plt.ylabel('Mz')
    plt.tick_params(direction= "inout",which="both")

    X, Y = np.meshgrid(xedges, yedges)
    p=ax.pcolormesh(X, Y, H,norm=colors.LogNorm(vmin=1, vmax=H.max()))
    plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")
    plt.xlim((7,1000))
    plt.ylim(mrange)
    cbar=plt.colorbar(p)
    cbar.ax.set_ylabel('dP/dMz dSNR')
    plt.show()
    plt.savefig("pics/v3/"+f+"_sample100000_3D.png",dpi=300)

#print("upps i did it again")
for a in range(0,4):
    print(a)
    f='SNRv3_mSU02_a'+str(a)+'_A8000'
    plotHist2D((5,300))
    plt.clf()
    f='SNRv3_mSU02_a'+str(a)+'_A800'
    plotHist2D((5,30))
    plt.clf()

#afas