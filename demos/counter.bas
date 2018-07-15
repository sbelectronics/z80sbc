10 REM all digits on
20 OUT &H0A, 0
30 A1=0
40 A2=0
50 S1=1
60 S2=1

100 GOSUB 5000
110 GOSUB 6000
120 A1=A1+S1
130 A2=A2+S2
140 GOTO 100

5000 REM query buttons for speed setting
5010 B=INP(&H0)
5020 IF (B and 8)=0 THEN S1=0
5030 IF (B and 4)=0 THEN S1=1
5040 IF (B and 2)=0 THEN S1=4
5050 IF (B and 1)=0 THEN S1=16
5060 IF (B and &H80)=0 THEN S2=0
5070 IF (B and &H40)=0 THEN S2=1
5080 IF (B and &H20)=0 THEN S2=4
5090 IF (B and &H10)=0 THEN S2=16
5100 RETURN

6000 REM display both counters
6010 X=A1
6020 GOSUB 7000
6030 OUT &H04, D0
6040 OUT &H06, D1
6050 X=A2
6060 GOSUB 7000
6070 OUT &H00, D0
6080 OUT &H02, D1
6090 RETURN

7000 REM compute digits from values in X
7050 D0=X\256
7060 X=X-(D0*256)
7070 D1=X
7080 RETURN