// Script:    caesarcipher.java
// Desc:      Encrypt and decrypt text with a Caesar cipher. Based on my Python version.
// Author:    Fraser Dumayne
// Created:   09/07/2017

package caesarcipher;

import java.util.Scanner; 

public class Caesarcipher {

	public static final String keyset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // Initialise available characters

	public static String encrypt(String phrase, int key) {

		phrase = phrase.toUpperCase(); // Convert to uppercase to compare with keyset
		String cipher = ""; // Empty string to hold new characters

		for (int i=0; i<phrase.length(); i++) { // Loop through all characters of phrase
			int oldCharPosition = keyset.indexOf(phrase.charAt(i)); // Return the position in the keyset of the character given in the phrase
			int newCharPosition = (key + oldCharPosition) % keyset.length(); // Return the position of the new character in the keyset
			char newChar = keyset.charAt(newCharPosition); // Return the character at the new position in the keyset
			cipher += newChar; // Add the new character to the cipher
		}
		return cipher;
	}

	public static String decrypt(String phrase, int key) {
		
		phrase = phrase.toUpperCase(); 
		String plaintext = ""; 
		
		for (int i=0; i<phrase.length(); i++) {
			int oldCharPosition = keyset.indexOf(phrase.charAt(i));
			int newCharPosition = (key - oldCharPosition)*(-1) % keyset.length(); // Return the position of the new character in the keyset, this time by taking away rather than adding
			if (newCharPosition < 0) {
				newCharPosition = newCharPosition + keyset.length(); // If the number is less than 0 then loop round to end of alphabet
			}
			char newChar = keyset.charAt(newCharPosition);
			plaintext += newChar; 
		}
		return plaintext;
	}

	public static void main(String[] args) {

		Scanner userinput = new Scanner(System.in); // Take user input

		System.out.println("Enter the phrase you would like to encrypt/decrypt: "); // Get a phrase
		String phrase = userinput.next();

		while (!phrase.matches("^[a-zA-Z]+$")) { // Check the phrase uses English characters
			System.out.println("Please enter English characters only.");
			phrase = userinput.next();
		}

		System.out.println("What key would you like to use?"); // Get a key to convert the phrase
		int key = userinput.nextInt();
		
		System.out.println("Would you like to encrypt or decrypt?"); // Choose between decryption and encryption
		String choice = userinput.next();
		choice = choice.toLowerCase(); // Convert to lower case to avoid multiple versions of same word in different cases

		while (true) { // Check user enters either encrypt or decrypt
			if (choice.equals("encrypt")) {
				System.out.println(encrypt(phrase, key));
				break;
			}
			else if (choice.equals("decrypt")){
				System.out.println(decrypt(phrase, key));
				break;
			}
			else {
				System.out.println("Please enter the phrase 'encrypt' or 'decrypt'");
				choice = userinput.next();
				choice = choice.toLowerCase();
			}
		}
	}
}