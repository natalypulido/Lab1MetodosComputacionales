#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double ranx;
double rany ;
double funcion;
double idt;
double respuesta;
int i;
int main(){
   	FILE *ar=fopen("resultados.txt","w+");

     funcion = 0;
    idt = 200000.0;


 for(i = 0; i< idt;i++){
    ranx = (double) rand()/RAND_MAX;
    rany = (double) rand()/RAND_MAX;
         if(exp(-ranx) - rany > 0){
                  funcion++;
                       }
         }
    
 respuesta = funcion/idt;
 printf("%f",respuesta);
 fprintf(ar,"El valor de la integral es: %f\n", respuesta);
}
