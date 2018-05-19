#include <iostream>
#include <string.h> 
#include <fstream>
using namespace std;
static const int branchNum = 26; //声明常量
static const int Max_Word_Len = 40; //声明常量 
static int i;
static int pos = 0; 
char worddump[Max_Word_Len+1];  
struct Trie_node
{
    //记录此处是否构成一个串。
     bool isStr; 
     //指向各个子树的指针,下标0-25代表26字符
     Trie_node *next[branchNum];
     Trie_node():isStr(false)
     {
         for(int i = 0; i<branchNum; i++)
            next[i] =NULL;
     }
 };

 class Trie
 {
 public:
     Trie();
     void insert(const char* word);
     void search(const char* word);
     int traverse(Trie_node *result,int i);
     void deleteTrie(Trie_node *root);
 private:
     Trie_node* root;
    
 };

 Trie::Trie()
 {
     root = new Trie_node();
 }

 void Trie::insert(const char *word)
 {
     Trie_node *location = root;
     while(*word)
     {
         if(location->next[*word-'a'] == NULL)
         {
             Trie_node *tmp = new Trie_node();
             location->next[*word-'a'] = tmp;
         }
         location = location->next[*word-'a']; 
         word++;
     }
     //到达尾部,即为一个字符串
     location->isStr = true; 
 }
 
 int Trie::traverse(Trie_node *result,int char_i)  
 {  
    
    if (result == NULL)  
        return 0;  
    if (result->isStr)  
    {  
        worddump[pos]='a'+char_i;
        worddump[pos+1]='\0';  
        printf("%s\n", worddump);   
    }
    else if(char_i>=0)
    {
        worddump[pos]='a'+char_i;
    }
    for (int i=0; i<branchNum; ++i)  
    {  
        pos++;  
        traverse(result->next[i],i); 
        pos--;  
    }  
    return 0;  
 }  
 void Trie::search(const char *word)
 {
     Trie_node *location = root;
     const char *ptr = word;
     while(*ptr && location)
     {
         location = location->next[*ptr-'a'];
         ptr++;
     }
     if(location != NULL && !(*ptr))
     {
         ptr = word;
         int pre_len = strlen(ptr);
         while(*ptr)
             worddump[pos++] = *ptr++;
        pos--;
        traverse(location,-1);
     }
     else
     {
        printf("no vaild word\n");
     }
 }

 void Trie::deleteTrie(Trie_node *root)
 {
     for(i = 0; i < branchNum; i++)
     {
         if(root->next[i] != NULL)
         {
             deleteTrie(root->next[i]);
         }
     }
     delete root;
 }


 int main(int argc, char *argv[])  
 {
     Trie t;
     char *set[] = {"llapp", "application","apple","apply","eyes","attation"};
     for(int i=0;i<5;i++)
       t.insert(set[i]);
     char pre[] = "木耳";//pre[] = argv[1] //"app"; 参数读取第一个
     t.search(pre);
     return 0;
 }
