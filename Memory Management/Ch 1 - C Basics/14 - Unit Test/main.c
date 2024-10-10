#include "../../munit/munit.h"
#include "exercise.h" // Include your header file with the `get_average` function
#include <math.h>     // For fabs function

// Define the test for get_average(3, 4, 5)
static MunitResult test_get_average(const MunitParameter params[], void *data) {
  float result = get_average(3, 4, 5);
  double expected = 4.0;
  double tolerance = 0.001;

  munit_assert(fabs(result - expected) <
               tolerance); // Use fabs for tolerance comparison
  return MUNIT_OK;
}

// Define the test for non-integer average
static MunitResult test_non_integer(const MunitParameter params[], void *data) {
  float result = get_average(3, 3, 5);
  double expected = 11.0 / 3.0; // Expected result: 3.66667
  double tolerance = 0.001;

  munit_assert(fabs(result - expected) < tolerance); // Compare with tolerance
  return MUNIT_OK;
}

// Define the test for the average of identical numbers
static MunitResult test_average_of_same(const MunitParameter params[],
                                        void *data) {
  float result = get_average(10, 10, 10);
  double expected = 10.0;
  double tolerance = 0.001;

  munit_assert(fabs(result - expected) < tolerance); // Compare with tolerance
  return MUNIT_OK;
}

// Define the test for the average of larger numbers
static MunitResult test_average_of_big_numbers(const MunitParameter params[],
                                               void *data) {
  float result = get_average(1050, 2050, 2075);
  double expected = 1725.0;
  double tolerance = 0.001;

  munit_assert(fabs(result - expected) < tolerance); // Compare with tolerance
  return MUNIT_OK;
}

// Register the test cases
static MunitTest tests[] = {
    {"/get_average", test_get_average, NULL, NULL, MUNIT_TEST_OPTION_NONE,
     NULL},
    {"/get_average_float", test_non_integer, NULL, NULL, MUNIT_TEST_OPTION_NONE,
     NULL},
    {"/get_average_same", test_average_of_same, NULL, NULL,
     MUNIT_TEST_OPTION_NONE, NULL},
    {"/get_average_big", test_average_of_big_numbers, NULL, NULL,
     MUNIT_TEST_OPTION_NONE, NULL},
    {NULL, NULL, NULL, NULL, MUNIT_TEST_OPTION_NONE,
     NULL} // Null-terminate the array
};

// Define the test suite
static const MunitSuite suite = {"/average_suite", // Name of the test suite
                                 tests,            // Array of test cases
                                 NULL,             // No sub-suites
                                 1,                // Number of iterations
                                 MUNIT_SUITE_OPTION_NONE};

// Main function to run the test suite
int main(int argc, char *argv[]) {
  return munit_suite_main(&suite, NULL, argc, argv);
}
