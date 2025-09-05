import java.util.Scanner;

public class estructuras_repetitivas{
    public static void main(String[] args) {
        /*
            for (int i = 2; i <= 50; i++) {

                boolean esPrimo = true;

                for (int j = 2; j <= i / 2; j++) {
                    if (i % j == 0) {
                        esPrimo = false;
                        break;
                    }
                }

                if (esPrimo) {
                    System.out.println(i + " es primo");
                }
            }
 
        
        
            int suma = 0;

            for (int i = 1; i <= 100; i++) {

                if (i % 3 == 0 || i % 5 == 0) {

                    suma += i;

                }

            }

            System.out.println( suma);
        */
    
        

        // Ejercicio 2.1: Tabla de Multiplicar de un Número
            // Escribir un programa en el cual se solicite al usuario un número y se imprima la tabla de multiplicar del 1 al 10 del valor introducido.

            /* 
                Scanner entrada = new Scanner(System.in);
                int numero;
                System.out.println("Ingrese un numero del 1 al 10: ");
                numero = entrada.nextInt();

                if(numero > 10){
                    System.out.println("El numero introdicido es mayor a 10");
                }else if(numero < 1){
                    System.out.println("El numero introdicido es menor a 1");
                }else{
                    System.out.println("La tabla del "+ numero+" es: ");

                    for(int i=1; i<11; i++){
                        int res = numero * i;
                        System.out.println(numero+" x "+i+" = "+res );
                    }
                }
            */
        

        // Ejercicio 2.2. Tabla de Potencias de un Número
            // Escribir un programa en el cual se solicite al usuario un número y se imprima la tabla de potencias del 1 al 10 del valor introducido.

            /* 
                Scanner entrada = new Scanner(System.in);
                int numero;
                System.out.println("Ingrese un numero del 1 al 10: ");
                numero = entrada.nextInt();

                if(numero > 10){
                    System.out.println("El numero introdicido es mayor a 10");
                }else if(numero < 1){
                    System.out.println("El numero introdicido es menor a 1");
                }else{
                    System.out.println("La tabla del "+ numero+" es: ");

                    for(int i=1; i<11; i++){
                        int res = (int) Math.pow(numero,i);
                        System.out.println(numero+" ^ "+i+" = "+res );
                    }
                }
            */

        // Ejercicio 2..3: Imprimir números de forma Creciente
            // Escribir un programa que imprima los números pares entre 0 y 200 de forma creciente.

            /* 
                for(int i=0;i < 200;i+=2){
                    System.out.print(i+", ");
                }
                System.out.print(200);
            */

        // Ejercicio 2.4: Imprimir números de forma Decreciente
            // Escribir un programa que imprima los números pares entre el 0 y 200 de forma decreciente.

                /* 
                    for(int i=200;i > 0;i-=2){
                        System.out.print(i+", ");
                    }
                    System.out.print(0);
                */

        // Ejercicio 2.5: Imprimir números pares hasta un número dado
            // Escribir un programa que imprima los números pares de forma creciente hasta un número introducido por el usuario.

                /* 
                    Scanner entrada= new Scanner(System.in);
                    int numero;
                    System.out.println("Ingrese un numero entero:");
                    numero = entrada.nextInt();

                    for(int i=0;i < numero;i+=2){
                        System.out.print(i+", ");
                    }

                    System.out.print(numero);
                */


        // Ejercicio 2.6: Números Primos
            // Escribir un programa que imprima todos los números primos hasta un número introducido por el usuario.

                /* 
                    Scanner entrada= new Scanner(System.in);
                    int numero;
                    System.out.print("Ingrese un numero entero: ");
                    numero = entrada.nextInt();                

                    for(int x = 2; x <= numero; x++){
                        int contador = 0;
                        for(int i=1; i <= x; i++){
                            if(x%i == 0){
                                contador++;
                            }           
                        }

                        if(contador < 3){
                            System.out.println(x);
                        }

                    }               
                */   
    }
}