from vpython import *

scene = canvas(background=vector(0, 0, 0), center=vector(0, -5, 0))


pos1 = vector(-4.5, 0, 0)
pos2 = vector(-3.5, 0, 0)
pos3 = vector(-2.5, 0, 0)
pos4 = vector(-1.5, 0, 0)
pos5 = vector(-0.5, 0, 0)
pos6 = vector(0.5, 0, 0)
pos7 = vector(1.5, 0, 0)
pos8 = vector(2.5, 0, 0)
pos9 = vector(3.5, 0, 0)
pos10 = vector(4.5, 0, 0)


block1 = box(pos=pos1, size=vector(0.5, 0.5, 0.5), color=color.cyan, opacity=0.8)
block2 = box(pos=pos2, size=vector(0.5, 0.5, 0.5), color=color.cyan, opacity=0.8)
block3 = box(pos=pos3, size=vector(0.5, 0.5, 0.5), color=color.cyan, opacity=0.8)
block4 = box(pos=pos4, size=vector(0.5, 0.5, 0.5), color=color.cyan, opacity=0.8)
block5 = box(pos=pos5, size=vector(0.5, 0.5, 0.5), color=color.cyan, opacity=0.8)
block6 = box(pos=pos6, size=vector(0.5, 0.5, 0.5), color=color.cyan, opacity=0.8)
block7 = box(pos=pos7, size=vector(0.5, 0.5, 0.5), color=color.cyan, opacity=0.8)
block8 = box(pos=pos8, size=vector(0.5, 0.5, 0.5), color=color.cyan, opacity=0.8)
block9 = box(pos=pos9, size=vector(0.5, 0.5, 0.5), color=color.cyan, opacity=0.8)
block10 = box(pos=pos10, size=vector(0.5, 0.5, 0.5), color=color.cyan, opacity=0.8)

wall = box(pos=vector(0, 0, 0), size=vector(10, 0.5, 7))

spring1 = helix(pos=pos1, radius=0.5, coils=8, thickness=0.1, color=color.gray(0.5))
spring2 = helix(pos=pos2, radius=0.5, coils=8, thickness=0.1, color=color.gray(0.5))
spring3 = helix(pos=pos3, radius=0.5, coils=8, thickness=0.1, color=color.gray(0.5))
spring4 = helix(pos=pos4, radius=0.5, coils=8, thickness=0.1, color=color.gray(0.5))
spring5 = helix(pos=pos5, radius=0.5, coils=8, thickness=0.1, color=color.gray(0.5))
spring6 = helix(pos=pos6, radius=0.5, coils=8, thickness=0.1, color=color.gray(0.5))
spring7 = helix(pos=pos7, radius=0.5, coils=8, thickness=0.1, color=color.gray(0.5))
spring8 = helix(pos=pos8, radius=0.5, coils=8, thickness=0.1, color=color.gray(0.5))
spring9 = helix(pos=pos9, radius=0.5, coils=8, thickness=0.1, color=color.gray(0.5))
spring10 = helix(pos=pos10, radius=0.5, coils=8, thickness=0.1, color=color.gray(0.5))

m1 = 0.164084334
m2 = 0.155377965
m3 = 0.147386644
m4 = 0.139385265
m5 = 0.132632241
m6 = 0.129414114
m7 = 0.126550411
m8 = 0.120352976
m9 = 0.115167217
m10 = 0.110888415

k1 = 4.498463303
k2 = 4.519193548
k3 = 4.540115741
k4 = 4.540115741
k5 = 4.561232558
k6 = 4.692177033
k7 = 4.830862069
k8 = 4.830862069
k9 = 4.854777228
k10 = 4.903325


y1= y2= y3= y4= y5= y6= y7= y8= y9= y10 = 2

v1= v2= v3= v4= v5= v6= v7= v8= v9= v10 = 0


t = 0
dt = 0.01

label = label()

while True:
   rate(100)
   t += dt

   a1 = -k1/m1 *y1
   a2 = -k2/m2 *y2
   a3 = -k3/m3 *y3
   a4 = -k4/m4 *y4
   a5 = -k5/m5 *y5
   a6 = -k6/m6 *y6
   a7 = -k7/m7 *y7
   a8 = -k8/m8 *y8
   a9 = -k9/m9 *y9
   a10 = -k10/m10 *y10

   v1 += a1*dt
   v2 += a2*dt
   v3 += a3*dt
   v4 += a4*dt
   v5 += a5*dt
   v6 += a6*dt
   v7 += a7*dt
   v8 += a8*dt
   v9 += a9*dt
   v10 += a10*dt

   y1 += v1*dt
   y2 += v2*dt
   y3 += v3*dt
   y4 += v4*dt
   y5 += v5*dt
   y6 += v6*dt
   y7 += v7*dt
   y8 += v8*dt
   y9 += v9*dt
   y10 += v10*dt

   block1.pos.y = y1 - 5
   block2.pos.y = y2 - 5
   block3.pos.y = y3 - 5
   block4.pos.y = y4 - 5
   block5.pos.y = y5 - 5
   block6.pos.y = y6 - 5
   block7.pos.y = y7 - 5
   block8.pos.y = y8 - 5
   block9.pos.y = y9 - 5
   block10.pos.y = y10 - 5

   spring1.axis = block1.pos - pos1
   spring2.axis = block2.pos - pos2
   spring3.axis = block3.pos - pos3
   spring4.axis = block4.pos - pos4
   spring5.axis = block5.pos - pos5
   spring6.axis = block6.pos - pos6
   spring7.axis = block7.pos - pos7
   spring8.axis = block8.pos - pos8
   spring9.axis = block9.pos - pos9
   spring10.axis = block10.pos - pos10

   label.pos = wall.pos + vector(0, 0, 0)
   label.text = 'time : %.2f s' % t