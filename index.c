
   
#include<stdio.h>

struct student{
   int id;
   char name[20];
   int sem;
   char sec;
   char group[5];
   char city[15];
   long phone;
   
};

int main(){
    
    struct student s[2];
    
    for(int i=0 ; i<2 ; i++){
        
        
        printf("Enter student system id:");
        scanf("%d",&s[i].id);
        
   
        printf("Enter student name:\n");
        scanf("%s",s[i].name);
        
        
        printf("Enter student sem:\n");
        scanf("%d",&s[i].sem);
        
        printf("Enter student group:\n");
        scanf("%s",s[i].group);
        
        printf("Enter student city:\n");
        scanf("%s",s[i].city);
        
        printf("Enter student sec:\n");
        scanf("%s",s[i].sec);
        
      
       
        
        // printf("Enter student phone no:\n");
        // scanf("%ld",&s[i].phone);
        
    }
        
        for(int i = 0; i<2 ; i++){
            
            printf("s.no:%d",i+1);
            printf("system id:%d\n",s[i].id);
            printf("name:%s\n",s[i].name);
            printf("section:%c\n",s[i].sec);
            printf("group:%s\n",s[i].group);
            printf("city:%s\n",s[i].city);
            // printf("phone:%ld",s[i].phone);
            
        }
        
        return 0;
        
      



        
    }