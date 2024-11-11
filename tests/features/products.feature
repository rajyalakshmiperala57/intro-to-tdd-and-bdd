Scenario: List all products
  Given I have a list of products
  When I request to see all products
  Then I should see a list of products
