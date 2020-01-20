

class Node{
	private:
		Node next = NULL;
		int data;

	public:
		Node(int d){
			data = d;
		}

		void appendToTail(int d){
			Node end = new Node(d);
			Node n = this;
			while(n.next != NULL){
				n = n.next;
			}
			n.next = end;
		}
}