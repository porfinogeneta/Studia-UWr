// szukamy pierwszego większego
int Upper(Node *node, int x) {

    if (node == NULL){
        return INT_MAX;
    }
    if (node->key == x){
        return node->key;
    }
    else if (x < node->key){
        // probujemy zacieśnić przedział
        int leftResult = Upper(node->left, x);
        if (x <= leftResult){
            return leftResult;
        }else {
            return node->key;
        }
        
    }
    // jak obecny korzeń jest za mały to idziemy na prawą gałąź
    else{
        Upper(node->right, x);
    }
    
}

// szukamy pierwszego mniejszego
int Lower(Node *node, int x) {

    if (node == NULL){
        return INT_MIN;
    }
    if (node->key == x){
        return node->key;
    }
    else if (x > node->key){
        // chcemy zacieśnić przedział
        int rightResult = Lower(node->right, x);
        
        if (x >= rightResult){
            return rightResult;
        }else {
            return node->key;
        }
        
    }
    else{
        Lower(node->left, x);
    }
}