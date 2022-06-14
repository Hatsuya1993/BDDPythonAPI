# Created by hal19 at 20/5/2022
Feature: Verify typicode endpoint

  Scenario: Verify typicode get posts
    Given the typicode get posts details
    When post endpoint is executed
    Then post response should displayed correctly

  Scenario: Verify typicode get single posts
    Given the typicode get single posts details
    When single post endpoint is executed
    Then single post response should be displayed correctly

  Scenario: Verify typicode get comments posts
    Given the typicode get posts comments details
    When comments post endpoint is executed
    Then comments post response should be displayed correctly


  Scenario: Verify typicode get comments for posts id 1
    Given the typicode get post id details
    When post id endpoint is executed
    Then comments should only display posts id 1


  Scenario Outline: Verify typicode post comments
    Given the typicode post comments details given <title> and <body>
    When comments with body post is executed
    Then comments should contain the same <title> and <body>
      Examples:
        | title | body |
        | "Hello title" | "Hello Body" |

  Scenario: Verify typicode get comments
    Given the typicode comment path params
    When typicode comment endpoint is executed
    Then comments endpoint should be displayed correctly