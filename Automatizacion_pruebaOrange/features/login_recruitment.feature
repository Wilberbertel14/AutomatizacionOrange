Feature: Login and access Recruitment

  Scenario: Successful login and access to recruitment
    Given I am on the login page
    When I enter username and password
    And I click on login
    And I navigate to Recruitment
    Then I should see the Recruitment page
    And I click on the Add button