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
    }
    else{
        Node* current = head->next;
        while (current != nullptr){
            current = current->next;
        }
        current = createNode(data);
        std::cout << "Added " << data << std::endl;
    }
    
    return head;
}

Node* deleteNode_recursive(Node* head, int data){
    
    if (head->data == data){
        Node* temp = head;
        head = temp->next;
        delete temp;
    }
    else{
        if (head->next->data == data){
            Node* temp = head->next;
            head->next = head->next->next;
            delete temp;
            return head;
        }
        else{
            head->next = deleteNode_recursive(head->next, data);
        }
    }
    return head;
}

Node* deleteNode(Node* head, int data){
    
    Node* current = head;

    if (head->data == data){
        delete head;
        head = head->next;
    }
    else{
        while (current->next != nullptr){
            if (current->next->data == data){
                Node* temp = current->next;
                current->next = current->next->next;
                delete temp;
                break;
            }
            else{
                current = current->next;
            }
        }
    }

    return head;
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

    cout << head->data << endl;
    cout << head->next->data << endl;

    /*
    head = insertNode(head, 20);
    head = insertNode(head, 30);

    cout << (head == nullptr) << endl;

    cout << head->data << endl;
    cout << head->next->data << endl;
    cout << head->next->next->data << endl;

    //printLL(head);
    //deleteLL(head);
    //printLL(head);
    */

    return 0;
}