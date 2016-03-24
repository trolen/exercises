#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void main(int argc, char *argv[]){
char B[160];FILE *f=fopen("snowman.dat","r");fread(B,sizeof(char),124,f);fclose(f);char *D[32];for(int i=0;i<32;i++){D[i]=strtok((i>0?0:B),"|");}
char *d(int n){return D[4*n+(argv[1][n]-'1')];}
printf(" %.5s\n %s\n%.1s(%s%s%s)%.1s\n%c(%.3s)%c\n (%.3s)\n\n",d(0),&d(0)[5],d(4),d(2),d(1),d(3),d(5),d(4)[1],d(6),d(5)[1],d(7));
}
