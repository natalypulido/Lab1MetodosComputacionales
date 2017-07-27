#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void condiciones_iniciales(double *u, double *u_cero, int numero_x, double delta_x);
//void primera_iteracion(double *u_presente, double *u_inicio, int numero_x, double r);
void actualizar(double *u_presente, double *u_inicio, int numero_x, double r); 
void copiar(double *u_nuevo, double *u_antiguo, int numero_x);
void imprimir_u(double *u, double *n_cero, int numero_x, double delta_x);
	
int main()
{

	double x_final = 2.0;
	int numero_x = 100;
	double delta_x = (x_final)/(numero_x-1.0);
	double t_final = 0.3;
	int numero_t = 300;
	double delta_t = (t_final)/(numero_t - 1);
	double c = 1.0;
	double r = c*(delta_t/delta_x);
	double *u_antiguo = malloc(numero_x*sizeof(double));
	double *u_presente = malloc(numero_x*sizeof(double));
	double *u_cero = malloc(numero_x*sizeof(double));
	FILE * fp;


	condiciones_iniciales(u_antiguo,u_cero,numero_x,delta_x);
	u_antiguo[0]=0;
	u_antiguo[numero_x-1]=0;

	int i;
	for (i=0;i<numero_t;i++)
	{
		actualizar(u_presente,u_antiguo,numero_x,r);
		copiar(u_presente,u_antiguo,numero_x);

	}
	
	//NO ME CORRIO BIEN EL METODO QUE USE PARA GUARDAR LOS DATOS EN UN TXT, POR ESO LO DEJE COMENTADO 
   /*fp = fopen ("misdatos.txt", "w+");
   fprintf(fp, );
   
   fclose(fp);
   
   return(0);*/

	imprimir_u(u_presente,u_cero,numero_x,delta_x);
	return 0;
}

void condiciones_iniciales(double *u, double *u_cero, int numero_x, double delta_x)
{
	int i;
	for(i=0;i<numero_x;i++)
	{
		double x = i*delta_x;
			if(x>=0.7 && x<=1.2)
			{
				u[i] =2;
				u_cero[i] =2;
			}
			else
			{
				u[i] =0;
				u_cero[i] =0;
			}
	}
}

void actualizar(double *u_presente, double *u_inicial, int numero_x, double r)
{
int i;
	for(i=1;i<numero_x-1;i++)
	{
	u_presente[i] =u_inicial[i]-r*(u_inicial[i]-u_inicial[i-1]);
	}
}


void copiar(double *u_nuevo,double *u_antiguo, int numero_x)
{
int i ;
	for(i=0;i<numero_x;i++)
	{
	u_antiguo[i] = u_nuevo[i];
	}
}

void imprimir_u(double *u,double *u_cero, int numero_x,double delta_x)
{
int i;
	for(i=0;i<numero_x;i++)
	{
	printf("%f %f %f\n",i*delta_x,u[i],u_cero[i]);
	}
}


