import java.util.Scanner;

public class TP4{
    public static void main(String[] args) {
        // 1. Muestre la longitud de una cadena de caracteres ingresado x teclado.
     
            Scanner entrada= new Scanner(System.in);

            System.out.print("Ingrese un texto: ");
            String cadena = entrada.nextLine();

            int longitud = cadena.length();
            System.out.println("- La cadena tiene "+ longitud + " caracteres");

        // 2: Elimina los espacios de una cadena ingresada.
    
            String espacios= cadena.replace(" ", "");
            System.out.println("- Cadena sin espacios: "+ espacios);

        // 3: Cuenta las vocales  de una String  ingresada.

            int contador = 0;

            char[] vocales={'a','e','i','o','u'};

            for(int i = 0; i< cadena.length(); i++){
                char letra = cadena.charAt(i);

                for(int x=0; x<5; x++){
                    if (letra == vocales[x]){
                        contador++;
                    }
                }
            }

            System.out.println("- La cadena tiene: "+ contador + " vocales");
        
        // 4 Transforma una cadena a mayúsculas. 

            String mayusculas = cadena.toUpperCase();
            System.out.println("- Cadena en mayusculas: "+ mayusculas);

        // 5: Compara dos cadenas ingresadas por teclado. Determinar sI son iguales.

            System.out.println("");
            System.out.print("Ingrese otra cadena: ");

            String cadena2 = entrada.nextLine();

            Boolean comparacion = cadena.equals(cadena2);

            if(comparacion == true){
                System.out.println("- Las cadenas son iguales");
            }else if(comparacion == false){
                System.out.println("- Las cadenas no son iguales");
            }

        // 6  Ingresar un nombre por teclado y mostrar con que letra comienza.

            System.out.println("");
            System.out.print("Ingrese un nombre: ");
            String nombre = entrada.nextLine();
            char primletra = nombre.charAt(0);

            System.out.println("- El nombre comienza con la letra: "+ primletra);

        // 7.  Ingresar una cadena que contenga un punto y muestre lo que hay después del punto.

            System.out.println("");
            System.out.print("Ingrese 2 oraciones separadas por un '.': ");

            String oraciones = entrada.nextLine();
            int punto = oraciones.indexOf(".");
            
            int largoOracion = oraciones.length();
            
            String segOracion = oraciones.substring(punto+1, largoOracion);

            System.out.println("- La segunda oracion es: "+ segOracion);

        // 8. contar la cantidad de palabras de una string.

            System.out.println("");
            String[] palabras = oraciones.split(" ");
            int cantPalabras = palabras.length;

            System.out.println("Hay "+ cantPalabras+ " palabras en la oracion");
    
        // 9 Ingresar una dirección de correo y verificar que la longitud no supere los 12 caracteres. Tenga un @ y termine en . Com

            String correo = null;

            Boolean longi = false;
            Boolean arr = false;
            Boolean terminacion = false;

            while (longi == false || arr == false || terminacion == false) {
                System.out.print("Ingrese un correo electronico: ");
                correo = entrada.nextLine();

                if(correo.length() < 13){
                    longi = true;
                }else{
                    System.out.println("El correo electrinico debe contener como maximo 12 caracteres");
                }

                Boolean arroba = correo.contains("@");
                if (arroba == true) {
                    arr = true;
                }else{
                    System.out.println("El correo electrinico debe contener un '@'");
                }

            
                int longCorreo = correo.length();
                int longCom = correo.lastIndexOf('.');

                String puntoCom = correo.substring(longCom+1, longCorreo);
                String termCorreo = "com";

                Boolean iguales = puntoCom.equals(termCorreo);


                if(iguales == true){
                    terminacion = true;
                }else{
                    terminacion = false;
                    System.out.println("El correo electrinico debe terminar en '.com' ");
                }

                if(longi == true && arr == true && terminacion == true){
                    System.out.println("El correo electronico es: "+ correo);
                }
            }
            
       
        // 10. El usuario ingresa una cadena hasta verificar que tenga longitud mayor que 8 y la primera letra comience en mayúscula, en este caso mostrará el mensaje "cadena correcta". 
        // Si no cumple alguna de las condiciones mostrará el mensaje "cadena incorrecta, vuelva a ingresar".

            
            Boolean largo = false;
            Boolean mayus = false;

            while (largo == false || mayus == false ) {
                System.out.print("Ingrese una cadena que empiece con mayuscula y tenga minimo 8 caracteres: ");
                String cad = entrada.nextLine();
                char primeraLetra = cad.charAt(0);

                if(cad.length() > 8){
                    largo = true;
                }else{
                    System.out.println("La cadena tiene que tener por lo menos 8 caracteres");
                }

                if(Character.isUpperCase(primeraLetra)){
                    mayus = true;
                }else{
                    System.out.println("La cadena debe empezar por una letra mayuscula");
                }

                if(largo == false || mayus == false){
                    System.out.println("cadena incorrecta, vuelva a ingresar");
                }

            }


            if(largo == true && mayus == true){
                System.out.println("cadena correcta");
            }
    }

}
