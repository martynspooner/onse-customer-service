Feature: Update customer


  Scenario: Updating existing customer
    Given customer "Joe Bloggs" with ID "333" exists
    When  customer id "333" changes name to "Joe Blogs"
    And   I fetch customer "333"
    Then  I should see customer "Joe Blogs"
