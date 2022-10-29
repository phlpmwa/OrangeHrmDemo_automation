
# Created by Phlp at 10/27/2022
  @smoke_test
Feature: login feature
  login should pass for correct details and
  fail for wrong details

  Scenario Outline: login with correct details
    Given user is on login page
    When user enter "<username>"
    Then  user enter "<password>"
    And  user user click login button
    Then home page should open
    Examples:
      | username | password |
      | Admin    | admin123 |
      | Phlp     | admin123 |


