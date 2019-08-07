int abs(int a){
	int b = a >> 31;
	return (b ^ a) - b;
}
