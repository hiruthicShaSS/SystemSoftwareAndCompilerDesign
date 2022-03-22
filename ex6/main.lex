%{
#include<stdio.h>
int id=0;
int totalToken = 0;
%}
%%
asm|double|new|switch|auto|else|operator|template|break|enum|private|this|case|extern|protected|throw|catch|float|public|try|char|for|register|typedef|class|friend|return|union|const|goto|short|unsigned|continue|if|signed|virtual|default|inline|sizedof|void|delete|int|static|volatile|do|long|struct|while {printf("<KEYWORD, "); ECHO; printf(" >"); totalToken++;}

[{};,()]   {printf("\n<Punctuation, "); ECHO; printf(" >"); totalToken++;}

[+-/=*%]   {printf("\n<OPERATOR, "); ECHO; printf(" >"); totalToken++;}

"END" {return -1;};

([a-zA-Z][0-9])+|[a-zA-Z]* {printf("\n<Identifier, "); ECHO; printf(" id=%d >",id+1); id++; totalToken++;}

.|\n ;
%%

int yywrap() {
    return 1;
}

int main(void) {
    yylex();
    printf("Total no of token in the program: %d",totalToken+1);
    return 0;
}
