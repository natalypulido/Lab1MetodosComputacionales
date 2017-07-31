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
   	FILE *ar=fopen("resultados.txt","a");

     funcion = 0;
    idt = 200000.0;


 for(i = 0; i< idt;i++){
    ranx = (double) rand()/RAND_MAX;
    rany = (double) rand()/RAND_MAX;

         if(ranx*ranx+rany*rany<1){
                  funcion++;
                       }
         }
    
 respuesta = 4*funcion/idt;
 printf("%f",respuesta);
 fprintf(ar,"El valor de la constante pi es: %f\n", respuesta);


}
