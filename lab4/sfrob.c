#include <stdio.h>
#include <stdlib.h>

int frobcmp(char* str1, char* str2) {
  while(*str1 != ' ' && *str2 != ' ') {
    if (((*str1 ^ 42) > (*str2 ^ 42) )|| *str2 == ' ') {
      return 1;
    }
    if (((*str2 ^ 42) > (*str1 ^ 42)) || *str1 == ' ') {
      return -1;
    }
	str1++;
	str2++;
  }
  return 0;
}

int comp(const void* str1, const void* str2) {
  return frobcmp(*(char**) str1, *(char**) str2);
}

void checkinputerror() {
  if (ferror(stdin)) {
    fprintf(stderr, "reading input error!");
    exit(1);
  }
}

void checkoutputerror() {
  if (ferror(stdout)) {
    fprintf(stderr, "outputing error!");
    exit(1);
  }
}

void checkmemerror1(char* mem) {

if (mem == NULL) {
      fprintf(stderr, "Memory is full; cant be allocated");
      exit(1);
    }

}
void checkmemerror2(char** mem) {
	if(mem ==NULL) {
	  fprintf(stderr, "Memory is full; cant be allocated");
	  exit(1);
	}
}

int main(void) {
  
  	char cha = getchar();
  	checkinputerror();

	int num_char = 0;
  	int num_word = 0;

  	char* arrchar = malloc(sizeof(char));
  	char** arrword = malloc(sizeof(char*));

  while (!feof(stdin)) {
    	arrchar[num_char] = cha ;

    	char* temp_arrcha = realloc(arrchar, (num_char+2) * sizeof(char));
    	checkmemerror1(temp_arrcha);
    	arrchar = temp_arrcha;
    	num_char++;

    if (cha == ' ') {
      arrword[num_word] = arrchar;

      char** temp_arrword = realloc(arrword, sizeof(char*) * (num_word+2));
      checkmemerror2(temp_arrword);
      arrword = temp_arrword;
      num_word++;
      num_char =0;
      arrchar = NULL;
      arrchar = malloc(sizeof(char));
    }

    else if (feof(stdin) && cha == ' ') { 
	printf("advcd");    	
        arrchar[num_char] = ' ';
        arrword[num_word] = arrchar;
        num_word++;
        break;
    }

    cha = getchar();
    checkinputerror();
  }

  qsort(arrword, num_word, sizeof(char*), comp);

  int i;
  for(i = 0; i < num_word; i++) {
	int n =0;
  	while(1) {
  		putchar(arrword[i][n]);
      		checkoutputerror();
  		if(arrword[i][n] == ' ') {
		  putchar(arrword[i][n]);
		  checkoutputerror();
  		  break;
  		}
		n++;
	  }
  }

  free(arrword);

  return 0;
}
