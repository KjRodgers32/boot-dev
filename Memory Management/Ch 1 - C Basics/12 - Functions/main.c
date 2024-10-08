#include <stdio.h>

int max_sneklang_memory(int max_threads, int memory_per_thread) {
  return max_threads * memory_per_thread;
}
int main() {
  int max_mem = max_sneklang_memory(4, 512);
  printf("This is the max memory in sneklang: %d\n", max_mem);
}
