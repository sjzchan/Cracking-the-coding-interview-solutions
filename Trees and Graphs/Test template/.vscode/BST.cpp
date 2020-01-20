#include <iostream>


struct Node{
    int data;
    Node* left;
    Node* right;
};

//Function to create a new node
Node* get_new_node(int data){
    Node* new_node = new Node;
    new_node->data = data;
    new_node->left = nullptr;
    new_node->right = nullptr;
    return new_node;
}

//Function to insert a new node
Node* insert(Node* root, int data){
    
    if (root == nullptr){
        root = get_new_node(data);
    }
    else if (data <= root->data){
        root->left = insert(root->left, data);
    }
    else{
        root->right = insert(root->right, data);
    }
    std::cout << "Inserted " << data << std::endl;

    return root;
}

Node* findMin(Node* root){


    
}

//Function to remove a node
Node* remove(Node* root, int data){
    
    //cases: 
    //1. Deleting a leaf
    //2. Deleting a node with one child
    //3. Deleting a node with two children

    if (root == nullptr){
        return root; //or nullptr, they are the same
    }
    else if (data < root->data){
        root->left = remove(root->left, data);
    }
    else if (data > root->data){
        root->right = remove(root->right, data);
    }
    else{
        //Found node to be deleted
        //Case 1: No children/leaf
        if (root->left == nullptr && root->right == nullptr){
            delete root;
            root = nullptr;
            return root;
        }
        //Case 2: 1 right child
        else if(root->left == nullptr){
            Node* temp = root;
            root = root->right;
            delete temp;
            return root;
        }
        //Case 2: 1 left child
        else if(root->right == nullptr){
            Node* temp = root;
            root = root->left;
            delete temp;
            return root;
        }
        //Case 3: 2 children
        else{
            Node* temp = findMin(root->right);
            root->data = temp->data;
            root->right = remove(root->right, temp->data);
        }
    }
}


//Search function
bool search(Node* root, int data){
    
    if (root == nullptr){
        return false;
    }
    else if (root->data == data){
        return true;
    }
    else if (root->data > data){
        return search(root->left, data);
    }
    else{
        return search(root->right, data);
    }
}

//Print all nodes in order function
void print_BST(Node* root){


}


int main(){

    //Create empty BST    
    Node* root = nullptr;

    //Add some nodes
    root = insert(root, 20);
    root = insert(root, 25);
    root = insert(root, 30);
    root = insert(root, 15);

    // Search for 2 numbers in the tree and two numbers not in the tree
    for (int x : {30, 15, 17, 27}){
        if (search(root, x) == true){
            std::cout << "Found " << x << std::endl;
        }
        else{
            std::cout << "Did not find " << x << std::endl;
        }
    }
    
    

    //Remove some nodes
    remove(root, 30);
    remove(root, 25);
    remove(root, 17);

    //Print BST
    print_BST(root);


    return 0;    
}


