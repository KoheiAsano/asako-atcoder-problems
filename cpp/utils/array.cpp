#define ARRAY_LENGTH(array) (sizeof(array) / sizeof(array[0]))

#define SORT(arr) sort(arr, arr + ARRAY_LENGTH(arr))
#define MAX(arr) *max_element(arr, arr + ARRAY_LENGTH(arr))
#define MAXID(arr) distance(arr,max_element(arr, arr + ARRAY_LENGTH(arr)))
#define MIN(arr) *min_element(arr, arr + ARRAY_LENGTH(arr))
#define MINID(arr) distance(arr,min_element(arr, arr + ARRAY_LENGTH(arr)))
#define NID(arr,x) distance(arr,find(arr, arr + ARRAY_LENGTH(arr),x))
