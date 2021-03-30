from math import *



class CALC:
#### 这里单位为mm,MHz,ohm
    def __init__(self, e0, s0,h0,fo,w0=0.06,z0=50):
        # w is the width of center conductor, d is the width of gap
        self.w0=w0
        self.e0 =e0
        self.s0 = s0
        self.h0=h0
        self.f0=fo
        self.z0=z0

#### ana
    ## w To Z0
    def analyse(self):

        a0=self.s0
        b0=self.s0+2*self.w0

        k=a0/b0
        kd=sqrt(1-k*k)
        sk=sqrt(k)
        skd=sqrt(kd)


        k1=pi*a0/(4*self.h0)
        k2=pi*b0/(4*self.h0)
        ex1=exp(k1*2)
        ex2=exp(k2*2)

        k1x= ((ex1-1) / (ex1+1)) / ((ex2-1) / (ex2+1))

        k1y= sqrt(1-k1x*k1x)

        sk1= sqrt(k1x)

        sk1d=sqrt(k1y)

        if k < 0.7:
            kk = 1 / (log(2 * (1+skd) / (1-skd)) / pi)
        else:
            kk = log(2 * (1+sk) / (1-sk)) / pi

        if k1x < 0.7:
            kk1 = 1 / (log(2 * (1+sk1d) / (1-sk1d)) / pi)
        else:
            kk1 = log(2 * (1+sk1) / (1-sk1)) / pi



        cc = kk1 / kk

        ef = (1+self.e0 * cc) / (1+cc)

        z = 60 * pi / ((kk+kk1) * sqrt(ef))



        kz = 1 / sqrt(ef)

        l4 = 30 * 1e10 * kz / (self.f0 * 1e6 * 4)

        return z,l4



#### syn
    ## Z0 To w
    def synthesis(self,frg=0):
        z0=self.z0
        a0 = self.s0
        b0 = a0 * 1.5
        bw = a0 * 0.02

        if z0 > 60:
            bw=a0 * 0.5

        ee = 1
        n = 0

        while ee > 0.001:
            k = a0 / b0
            kd = sqrt(1-k * k)
            sk = sqrt(k)
            skd= sqrt(kd)

            k1 = pi * a0 / (4 * self.h0)
            k2 = pi * b0 / (4 * self.h0)
            ex1= exp(k1 * 2)
            ex2= exp(k2 * 2)
            k1x= ((ex1-1) / (ex1+1)) / ((ex2-1) / (ex2+1))

            k1y= sqrt(1-k1x * k1x)

            sk1= sqrt(k1x)
            sk1d=sqrt(k1y)

            if k < 0.7:
                kk = 1 / (log(2 * (1+skd) / (1-skd)) / pi)
            else:
                kk = log(2 * (1+sk) / (1-sk)) / pi

            if k1x < 0.7:
                kk1 = 1 / (log(2 * (1+sk1d) / (1-sk1d)) / pi)
            else:
                kk1 = log(2 * (1+sk1) / (1-sk1)) / pi


            cc = kk1 / kk

            ef = (1+self.e0 * cc) / (1+cc)

            z = 60 * pi / ((kk+kk1) * sqrt(ef))



            err= z-z0

            ee =abs(err)

            if n == 0:
                n = 1
                if err > 0:
                    frg= 0
                else:
                    frg= 1

            if err > 0:

                if frg == 0:
                    b0 = b0-bw
                else:
                    frg = 0
                    bw = bw / 2
            else:
                if frg == 1:
                    b0 = b0+bw

                else:
                    frg = 1
                    bw = bw / 2


            ww = (b0 - a0) / 2

            eff = ef

            kz = 1 / sqrt(ef)

            kz = kz

            l4 = 30 * 1e10 * kz / (self.f0 * 1e6 * 4)
        return l4,ww


if __name__=='__main__':
    e0 = 11.9

    s0 = 0.01  # Unit=mm

    w0 = 0.006  # Unit=mm

    h0 = 0.45  # Unit=mm

    f0 = 6500  # MHZ


    a=CALC(e0,s0,h0,f0,w0)
    a.analyse()
    a.synthesis()
