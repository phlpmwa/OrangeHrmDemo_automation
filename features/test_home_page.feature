# Created by Phlp at 10/29/2022
Feature: Test home page
  # Enter feature description here

  Scenario: go to admin page
    Given user is logged in
    When home page is opened
    And user click admin link
    Then admin page is opened