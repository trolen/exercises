#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void main(int argc, char *argv[]){char *D[]={"     _===_ ___ .....  _   /_\\  ___ (_*_)",",._ ",".oO ",".oO "," <\\  /  "," >/  \\  "," : ] [> <   "," : \" \"___   "};char *d(int n){char *B=(char *)calloc(16,sizeof(char));int l=strlen(D[n])/4,s=l*(argv[1][n]-'1');return strncpy(B,&D[n][s],l);}printf(" %.5s\n %s\n%.1s(%s%s%s)%.1s\n%c(%.3s)%c\n (%.3s)\n\n",d(0),&d(0)[5],d(4),d(2),d(1),d(3),d(5),d(4)[1],d(6),d(5)[1],d(7));}
