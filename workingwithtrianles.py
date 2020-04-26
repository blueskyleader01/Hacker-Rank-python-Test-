import math
# Enter your code here. Read input from STDIN. Print output to STDOUT
opposite = int(input())
adjacent = int(input())
hypothenus  =  math.sqrt(opposite**2+adjacent**2)
hyp_mid = hypothenus // 2 

angle_b_c_a = math.atan(opposite/adjacent)
angle_b_a_c = math.atan(adjacent/opposite)

#converting to degrees
# angle_b_a_c = round((angle_b_a_c*180)/math.pi)
# angle_b_c_a = round((angle_b_c_a*180)/math.pi)

# print(angle_b_c_a)
# print(angle_b_a_c)


bm = hyp_mid * math.degrees(math.tan(angle_b_c_a))
sin_m_b_c = (hyp_mid * math.degrees(math.sin(angle_b_c_a))) /bm
angle_m_b_c = math.asin(sin_m_b_c)
angle_m_b_c = 90 - round(math.degrees(angle_m_b_c))

print(angle_m_b_c,'\xb0',sep="")