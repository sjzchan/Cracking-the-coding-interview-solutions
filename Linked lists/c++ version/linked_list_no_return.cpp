#include <iostream>


struct Node{
    int data;
    Node* next;
};

Node* createNode(int data){
    Node* newNode = new Node;
    newNode->data = data;
    newNode->next = nullptr;
    
    return newNode;
}

Node* insertNode(Node* head, int data){
    if (head == nullptr){
        head = createNode(data);
        std::cout << "Added " << data << std::endl;
        return head;
    }
    else{
        return insertNode(head->next, data);
    }
}

Node* deleteNode(Node* head, int data){
    if (head == nullptr){
        return head;
    }
    else{
        if (head->data == data){
            Node* temp = head->next;
            delete head;
            head = temp;
            return head;
        }
        else{
            return deleteNode(head->next, data);
        }
    }
}

void printLL(Node* head){
    
    Node* current = head;
    int count = 1;
    while (current != nullptr){
        std::cout << count << ": " << current->data << std::endl;
        current = current->next;
        count++;
    }
}

void searchLL(Node* head, int data){
    
    Node* current = head;
    while (current != nullptr){
        if (current->data == data){
            std::cout << "Found" << std::endl;
            break;
        }
        else{
            current = current->next;
        }
    }
}

void deleteLL(Node* head){

    while (head != nullptr){
        Node* temp = head->next;
        delete head;
        head = temp;        
    }

    std::cout << "Linked list deleted" << std::endl;
}


int main(){

    using namespace std;

    Node* head = nullptr;
    
    head = insertNode(head, 10);
    head = insertNode(head, 20);
    head = insertNode(head, 30);

    printLL(head);
    deleteLL(head);
    printLL(head);

    return 0;
}