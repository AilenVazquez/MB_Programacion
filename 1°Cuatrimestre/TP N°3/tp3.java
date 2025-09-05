import java.util.Scanner;

import javax.swing.JOptionPane;

public class tp3{
    public static void main(String[] args) {
        //Ejercicio 1: Potencia de un número
            //Pedir al usuario que ingrese una base y un exponente, y calcular el resultado usando Math.pow.

            /* 
                Scanner entrada= new Scanner(System.in);
                int numero, exponente;

                System.out.println("Ingrese un número");
                numero = entrada.nextInt();

                System.out.println("Ingrese una exponente");
                exponente = entrada.nextInt();

                int res = (int) Math.pow(numero,exponente);

                System.out.println(" El resultado es: "+ res);
            */

        //Ejercicio 2: Valor absoluto
            //Solicitar al usuario un número entero (positivo o negativo) y mostrar su valor absoluto utilizando Math.abs
        
            /* 
                Scanner entrada = new Scanner(System.in);
                int numEnt;
                System.out.println("Ingrese un numero entero positivo o negativo: ");
                numEnt = entrada.nextInt();
                
                int absoluto = Math.abs(numEnt);
                System.out.println("El numero abosuluto de "+ numEnt+ " es: "+ absoluto);
            */
    
        //Ejercicio 3: Cálculo de distancia entre dos puntos
            //Solicitá al usuario las coordenadas de dos puntos en el plano (x1, y1) y (x2, y2). Calculá y mostrale la distancia entre ambos usando la fórmula:
            
            /* 
                Scanner entrada = new Scanner(System.in);
                int x1, x2, y1, y2;

                System.out.println("Ingrese 2 cordenadas del primer punto en el plano (x1, y1): ");
                x1 = entrada.nextInt();
                y1 = entrada.nextInt();

                System.out.println("Ingrese 2 cordenadas del segundo punto en el plano (x2, y2): ");
                x2 = entrada.nextInt();
                y2 = entrada.nextInt();

                int resta1 = x2-x1;
                int resta2 = y2-y1;
                int potencia1 = (int) Math.pow(resta1,2);
                int potencia2 = (int) Math.pow(resta2,2);

                int suma = potencia1+potencia2;

                int distancia = (int) Math.sqrt(suma);

                System.out.println("La distancia entre ambos puntos es: "+ distancia);
            */
    
        //Ejercicio 4: Ecuación de segundo grado
            //Pedí al usuario los coeficientes a, b y c de una ecuación cuadrática, y calculá las raíces reales utilizando la fórmula general:

            //Considerá los casos en los que las raíces no existen (discriminante negativo).

            /*
                Scanner entrada = new Scanner(System.in);

                int a, b, c;

                System.out.println("ingrese el valor de a");
                a = entrada.nextInt();

                System.out.println("ingrese el valor de b");
                b = entrada.nextInt();

                System.out.println("ingrese el valor de c");
                c = entrada.nextInt();

                Double interRaiz = Math.pow(b, 2) - (4*a*c);

                if (interRaiz < 0) {
                    System.out.println("La ecuacion no es posible de realizar");
                }else{
                    Double raiz = Math.sqrt(interRaiz);

                    Double x = (-(b) + raiz) / (2*a);

                    if (x < 0) {
                        System.out.println("La ecuacion no es posible de realizar");
                    }else{
                        System.out.println("La ecuacion da: "+ x);
                    }
                    
                }
            */
            

        //Ejercicio 5: Simulación de dados
            //Simulá el lanzamiento de dos dados utilizando Math.random(), y mostrá el resultado de ambos lanzamientos y su suma. Simulá 1000 lanzamientos y contá cuántas veces se obtiene cada posible suma (entre 2 y 12).
    
                int dos = 0;
                int tres = 0;
                int cuatro = 0;
                int cinco = 0;
                int seis = 0;
                int siete = 0;
                int ocho = 0;
                int nueve = 0;
                int diez = 0;
                int once = 0;
                int doce = 0;

                for(int i = 0;i <1000;i++){
                    

                    System.out.println("Se lanzaran 2 dados:");

                    int dado1 = 2/* MINIMO */ + (int)(Math.random() * (13/* MAXIMO+1 */ - 2/* MINIMO */));
                    int dado2 = 2 + (int)(Math.random() * (13 - 2));
                    int suma = dado1 + dado2;

                    System.out.println("El primer dado es: "+ dado1);
                    System.out.println("El primer dado es: "+ dado2);
                    System.out.println("La suma de ambos dados es: "+ suma);
                    System.out.println("------------------------");

                    if(suma == 4){
                        cuatro++;
                    }else if(suma == 5){
                        cinco++;
                    }else if(suma == 6){
                        seis++;
                    }else if(suma == 7){
                        siete++;
                    }else if(suma == 8){
                        ocho++;
                    }else if(suma == 9){
                        nueve++;
                    }else if(suma == 10){
                        diez++;
                    }else if(suma == 11){
                        once++;
                    }else if(suma == 12){
                        doce++;
                    }
                }

                System.out.println("Se obtuvo "+ cuatro + " veces el n°4");
                System.out.println("Se obtuvo "+ cinco + " veces el n°5");
                System.out.println("Se obtuvo "+ seis + " veces el n°6");
                System.out.println("Se obtuvo "+ siete + " veces el n°7");
                System.out.println("Se obtuvo "+ ocho + " veces el n°8");
                System.out.println("Se obtuvo "+ nueve + " veces el n°9");
                System.out.println("Se obtuvo "+ diez + " veces el n°10");
                System.out.println("Se obtuvo "+ once + " veces el n°11");
                System.out.println("Se obtuvo "+ doce + " veces el n°12");          


        //Ejercicio 6: Hipotenusa de un triángulo
            //Pedir al usuario los dos catetos de un triángulo rectángulo y calcular la hipotenusa usando el teorema de Pitágoras con Math.sqrt y Math.pow.

            /* 
                Scanner entrada = new Scanner(System.in);
                double cateto1, cateto2;

                System.out.println("CALCULO DE LA HIPOTENUSA: ");

                System.out.println("Ingrese la medida del primer cateto: ");
                cateto1 = entrada.nextDouble();

                System.out.println("Ingrese la medida del segundo cateto: ");
                cateto2 = entrada.nextDouble();

                double potencia = Math.pow(cateto1,2) + Math.pow(cateto2, 2);
                double hipotenusa = Math.sqrt(potencia);
                
                System.out.println("La Hipotenusa es " + hipotenusa);
            */

    }

}