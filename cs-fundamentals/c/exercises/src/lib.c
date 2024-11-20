// DOESN'T WORK >10 BC NEED TO WRITE MULTIPLE DIGITS

void generate_fizzbuzz(char buffer[], size_t buflen, int n) {
  size_t offset = 0;
  for (int i = 1; i <= n; i++) {
    if (i % 15 == 0) {
      snprintf(buffer+offset, buflen-offset, "%s", "FIZZBUZZ");
      offset += 8;
    } else {
      if (i % 3 == 0) {
        snprintf(buffer+offset, buflen-offset, "%s", "FIZZ");
        offset += 4;
      } else if (i % 5 == 0) {
        snprintf(buffer+offset, buflen-offset, "%s", "BUZZ");
        offset += 4;
      } else {
        snprintf(buffer+offset, buflen-offset, "%d", i);
        offset += 1;
      }
    }
    // Extra ", " except for last
    if (i < n) {
      snprintf(buffer+offset, buflen-offset, "%s", ", ");
      offset += 2;
    }
  }
}
