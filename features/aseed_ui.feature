Feature: ASEED Page UI Testing
  As a QA tester
  I want to thoroughly test all UI elements on the ASEED organization page
  So that I can ensure the page functions correctly and displays properly

  Background:
    Given the user is logged in with valid credentials
    When the user searches for "ASEED" and navigates to it

  # ========================================
  # PAGE LOAD & BASIC VISIBILITY (10 tests)
  # ========================================

  @aseed-ui @smoke
  Scenario: Verify ASEED page loads successfully
    Then the ASEED page should be loaded
    And the page URL should contain "/org/"
    And the page title should not be empty

  @aseed-ui
  Scenario: Verify page breadcrumb is visible
    Then the breadcrumb should show "ASEED"
    And the breadcrumb should show "Overview"

  @aseed-ui
  Scenario: Verify organization name is displayed
    Then the organization name "ASEED" should be visible
    And the organization name should be in large text

  @aseed-ui
  Scenario: Verify created date is displayed
    Then the created date should be visible
    And the created date should contain "Created:"

  @aseed-ui
  Scenario: Verify updated date is displayed
    Then the updated date should be visible
    And the updated date should contain "Updated:"

  @aseed-ui
  Scenario: Verify ElasticM2M logo is displayed
    Then the ElasticM2M logo should be visible
    And the logo should have alt text

  @aseed-ui
  Scenario: Verify page layout is responsive
    Then the page should have a responsive layout
    And all main sections should be visible

  @aseed-ui
  Scenario: Verify page background color
    Then the page background should be white or light colored

  @aseed-ui
  Scenario: Verify content area width
    Then the content area should have appropriate width
    And the content should be centered

  @aseed-ui
  Scenario: Verify page scrollability
    Then the page should be scrollable if content exceeds viewport

  # ========================================
  # HEADER/NAVIGATION (15 tests)
  # ========================================

  @aseed-ui @header
  Scenario: Verify menu button is visible
    Then the menu button should be visible in the header
    And the menu button should have a hamburger icon

  @aseed-ui @header
  Scenario: Verify menu button is clickable
    When the user clicks the menu button
    Then the side menu should open

  @aseed-ui @header
  Scenario: Verify search button in header is visible
    Then the search button should be visible in the header

  @aseed-ui @header
  Scenario: Verify search button in header is clickable
    When the user clicks the search button in the header
    Then the search input should appear

  @aseed-ui @header
  Scenario: Verify user profile button is visible
    Then the user profile button "Divya Bika" should be visible
    And the profile button should have a dropdown icon

  @aseed-ui @header
  Scenario: Verify user profile dropdown opens
    When the user clicks the profile button
    Then the profile dropdown menu should open

  @aseed-ui @header
  Scenario: Verify notifications icon is visible
    Then the notifications icon should be visible in the header

  @aseed-ui @header
  Scenario: Verify notifications icon is clickable
    When the user clicks the notifications icon
    Then the notifications panel should open or show count

  @aseed-ui @header
  Scenario: Verify header has dark background
    Then the header should have a dark background color
    And the header text should be light colored

  @aseed-ui @header
  Scenario: Verify header is sticky
    When the user scrolls down the page
    Then the header should remain fixed at the top

  @aseed-ui @header
  Scenario: Verify breadcrumb navigation works
    When the user clicks on "ASEED" in breadcrumb
    Then the page should navigate or refresh

  @aseed-ui @header
  Scenario: Verify breadcrumb separator is visible
    Then the breadcrumb should have a separator between items

  @aseed-ui @header
  Scenario: Verify header height is consistent
    Then the header should have a fixed height
    And the header should not overlap content

  @aseed-ui @header
  Scenario: Verify header icons alignment
    Then all header icons should be properly aligned
    And header elements should have proper spacing

  @aseed-ui @header
  Scenario: Verify header responsive behavior
    When the viewport is resized
    Then the header should adapt responsively

  # ========================================
  # TABS NAVIGATION (10 tests)
  # ========================================

  @aseed-ui @tabs
  Scenario: Verify Overview tab is visible
    Then the "OVERVIEW" tab should be visible
    And the "OVERVIEW" tab should be active

  @aseed-ui @tabs
  Scenario: Verify Payment Assurance tab is visible
    Then the "PAYMENT ASSURANCE" tab should be visible
    And the "PAYMENT ASSURANCE" tab should not be active

  @aseed-ui @tabs
  Scenario: Verify Mike Dashboard tab is visible
    Then the "MIKE DASHBOARD" tab should be visible
    And the "MIKE DASHBOARD" tab should not be active

  @aseed-ui @tabs
  Scenario: Verify clicking Payment Assurance tab
    When the user clicks on "PAYMENT ASSURANCE" tab
    Then the "PAYMENT ASSURANCE" tab should become active
    And the tab content should change

  @aseed-ui @tabs
  Scenario: Verify clicking Mike Dashboard tab
    When the user clicks on "MIKE DASHBOARD" tab
    Then the "MIKE DASHBOARD" tab should become active
    And the tab content should change

  @aseed-ui @tabs
  Scenario: Verify active tab has underline
    Then the active tab should have an underline indicator

  @aseed-ui @tabs
  Scenario: Verify inactive tabs are clickable
    Then all inactive tabs should be clickable

  @aseed-ui @tabs
  Scenario: Verify tab text styling
    Then all tabs should have uppercase text
    And tabs should have consistent font size

  @aseed-ui @tabs
  Scenario: Verify tabs horizontal alignment
    Then all tabs should be aligned horizontally
    And tabs should have equal spacing

  @aseed-ui @tabs
  Scenario: Verify tabs are responsive
    When the viewport width changes
    Then tabs should remain visible and accessible

  # ========================================
  # LOGO SECTION (10 tests)
  # ========================================

  @aseed-ui @logo
  Scenario: Verify logo placeholder is visible
    Then the logo placeholder should be visible
    And the placeholder should show a default image icon

  @aseed-ui @logo
  Scenario: Verify upload logo button is visible
    Then the "UPLOAD A CUSTOM LOGO" button should be visible

  @aseed-ui @logo
  Scenario: Verify upload logo button styling
    Then the upload button should have raised styling
    And the button should have primary color

  @aseed-ui @logo
  Scenario: Verify upload logo button is clickable
    When the user clicks "UPLOAD A CUSTOM LOGO" button
    Then a file upload dialog or modal should appear

  @aseed-ui @logo
  Scenario: Verify logo section has border
    Then the logo section should have a dashed border

  @aseed-ui @logo
  Scenario: Verify logo section dimensions
    Then the logo section should have square or near-square dimensions

  @aseed-ui @logo
  Scenario: Verify logo placeholder icon
    Then the placeholder should show an image icon
    And the icon should be centered

  @aseed-ui @logo
  Scenario: Verify hover effect on logo section
    When the user hovers over the logo section
    Then there should be a visual feedback

  @aseed-ui @logo
  Scenario: Verify logo section alignment
    Then the logo section should be left-aligned
    And it should be in the organization details area

  @aseed-ui @logo
  Scenario: Verify upload button text is all caps
    Then the upload button text should be in uppercase

  # ========================================
  # ORGANIZATION TAGS (10 tests)
  # ========================================

  @aseed-ui @tags
  Scenario: Verify Dealer tag is visible
    Then the "Dealer" tag should be visible
    And the tag should have orange/primary color

  @aseed-ui @tags
  Scenario: Verify Stolen Vehicle Recovery tag is visible
    Then the "Stolen Vehicle Recovery" tag should be visible
    And the tag should have purple/secondary color

  @aseed-ui @tags
  Scenario: Verify Payment Assurance tag is visible
    Then the "Payment Assurance" tag should be visible
    And the tag should have blue/tertiary color

  @aseed-ui @tags
  Scenario: Verify tags are displayed horizontally
    Then all tags should be displayed in a horizontal row
    And tags should have spacing between them

  @aseed-ui @tags
  Scenario: Verify tag styling and borders
    Then each tag should have rounded corners
    And each tag should have a colored border

  @aseed-ui @tags
  Scenario: Verify tag text styling
    Then tag text should be readable
    And tag text should match border color

  @aseed-ui @tags
  Scenario: Verify tags are not clickable
    When the user clicks on a tag
    Then nothing should happen or tag details should show

  @aseed-ui @tags
  Scenario: Verify tag positioning
    Then tags should be below the organization name
    And tags should be above the date information

  @aseed-ui @tags
  Scenario: Verify tag responsive behavior
    When the viewport is narrow
    Then tags should wrap to next line if needed

  @aseed-ui @tags
  Scenario: Verify all three tags are present
    Then there should be exactly 3 tags displayed
    And all tags should be visible simultaneously

  # ========================================
  # DASHBOARD CARDS - Loans (8 tests)
  # ========================================

  @aseed-ui @cards @loans
  Scenario: Verify Loans card is visible
    Then the "Loans" card should be visible
    And the card should display the count "0"

  @aseed-ui @cards @loans
  Scenario: Verify Loans card icon
    Then the Loans card should have a bank/institution icon
    And the icon should be white on dark background

  @aseed-ui @cards @loans
  Scenario: Verify Loans card count styling
    Then the Loans count should be in large font
    And the count should be centered above the label

  @aseed-ui @cards @loans
  Scenario: Verify Loans card label
    Then the Loans card should have "Loans" label
    And the label should be below the count

  @aseed-ui @cards @loans
  Scenario: Verify Loans card is clickable
    When the user clicks on the Loans card
    Then the user should navigate to Loans section or see Loans list

  @aseed-ui @cards @loans
  Scenario: Verify Loans card background color
    Then the Loans card should have a dark gray background

  @aseed-ui @cards @loans
  Scenario: Verify Loans card hover effect
    When the user hovers over the Loans card
    Then the card should show a hover effect

  @aseed-ui @cards @loans
  Scenario: Verify Loans card dimensions
    Then the Loans card should have consistent size with other cards

  # ========================================
  # DASHBOARD CARDS - Assets (8 tests)
  # ========================================

  @aseed-ui @cards @assets
  Scenario: Verify Assets card is visible
    Then the "Assets" card should be visible
    And the card should display the count "1"

  @aseed-ui @cards @assets
  Scenario: Verify Assets card icon
    Then the Assets card should have a tag icon
    And the icon should be white on blue background

  @aseed-ui @cards @assets
  Scenario: Verify Assets card count styling
    Then the Assets count should be in large font
    And the count should be prominently displayed

  @aseed-ui @cards @assets
  Scenario: Verify Assets card label
    Then the Assets card should have "Assets" label

  @aseed-ui @cards @assets
  Scenario: Verify Assets card is clickable
    When the user clicks on the Assets card
    Then the user should navigate to Assets section

  @aseed-ui @cards @assets
  Scenario: Verify Assets card background color
    Then the Assets card should have a blue background

  @aseed-ui @cards @assets
  Scenario: Verify Assets card shows non-zero count
    Then the Assets count should be "1"
    And the count should be greater than zero

  @aseed-ui @cards @assets
  Scenario: Verify Assets card hover effect
    When the user hovers over the Assets card
    Then there should be visual feedback

  # ========================================
  # DASHBOARD CARDS - Recovery Orders (8 tests)
  # ========================================

  @aseed-ui @cards @recovery
  Scenario: Verify Recovery Orders card is visible
    Then the "Recovery Orders" card should be visible
    And the card should display the count "1"

  @aseed-ui @cards @recovery
  Scenario: Verify Recovery Orders card icon
    Then the Recovery Orders card should have a truck icon

  @aseed-ui @cards @recovery
  Scenario: Verify Recovery Orders card count
    Then the Recovery Orders count should be "1"

  @aseed-ui @cards @recovery
  Scenario: Verify Recovery Orders card label
    Then the card should have "Recovery Orders" label

  @aseed-ui @cards @recovery
  Scenario: Verify Recovery Orders card is clickable
    When the user clicks on the Recovery Orders card
    Then the user should navigate to Recovery Orders section

  @aseed-ui @cards @recovery
  Scenario: Verify Recovery Orders card background
    Then the Recovery Orders card should have a blue background

  @aseed-ui @cards @recovery
  Scenario: Verify Recovery Orders card positioning
    Then the Recovery Orders card should be in the top row
    And it should be the third card from left

  @aseed-ui @cards @recovery
  Scenario: Verify Recovery Orders card hover
    When the user hovers over Recovery Orders card
    Then visual feedback should be displayed

  # ========================================
  # DASHBOARD CARDS - Vehicles (8 tests)
  # ========================================

  @aseed-ui @cards @vehicles
  Scenario: Verify Vehicles card is visible
    Then the "Vehicles" card should be visible
    And the card should display the count "0"

  @aseed-ui @cards @vehicles
  Scenario: Verify Vehicles card icon
    Then the Vehicles card should have a car icon

  @aseed-ui @cards @vehicles
  Scenario: Verify Vehicles card count
    Then the Vehicles count should be "0"

  @aseed-ui @cards @vehicles
  Scenario: Verify Vehicles card label
    Then the card should have "Vehicles" label

  @aseed-ui @cards @vehicles
  Scenario: Verify Vehicles card is clickable
    When the user clicks on the Vehicles card
    Then the user should navigate to Vehicles section

  @aseed-ui @cards @vehicles
  Scenario: Verify Vehicles card background
    Then the Vehicles card should have a dark gray background

  @aseed-ui @cards @vehicles
  Scenario: Verify Vehicles card positioning
    Then the Vehicles card should be in the second row
    And it should be the first card from left

  @aseed-ui @cards @vehicles
  Scenario: Verify Vehicles zero count display
    Then the zero count should be displayed clearly
    And it should not show as empty

  # ========================================
  # DASHBOARD CARDS - Media (8 tests)
  # ========================================

  @aseed-ui @cards @media
  Scenario: Verify Media card is visible
    Then the "Media" card should be visible
    And the card should display the count "0"

  @aseed-ui @cards @media
  Scenario: Verify Media card icon
    Then the Media card should have a play button icon

  @aseed-ui @cards @media
  Scenario: Verify Media card count
    Then the Media count should be "0"

  @aseed-ui @cards @media
  Scenario: Verify Media card label
    Then the card should have "Media" label

  @aseed-ui @cards @media
  Scenario: Verify Media card is clickable
    When the user clicks on the Media card
    Then the user should navigate to Media section

  @aseed-ui @cards @media
  Scenario: Verify Media card background
    Then the Media card should have a blue background

  @aseed-ui @cards @media
  Scenario: Verify Media card icon is centered
    Then the Media icon should be centered in the card

  @aseed-ui @cards @media
  Scenario: Verify Media card hover effect
    When the user hovers over Media card
    Then visual feedback should appear

  # ========================================
  # DASHBOARD CARDS - Geofences (8 tests)
  # ========================================

  @aseed-ui @cards @geofences
  Scenario: Verify Geofences card is visible
    Then the "Geofences" card should be visible
    And the card should display the count "0"

  @aseed-ui @cards @geofences
  Scenario: Verify Geofences card icon
    Then the Geofences card should have a map icon

  @aseed-ui @cards @geofences
  Scenario: Verify Geofences card count
    Then the Geofences count should be "0"

  @aseed-ui @cards @geofences
  Scenario: Verify Geofences card label
    Then the card should have "Geofences" label

  @aseed-ui @cards @geofences
  Scenario: Verify Geofences card is clickable
    When the user clicks on the Geofences card
    Then the user should navigate to Geofences section

  @aseed-ui @cards @geofences
  Scenario: Verify Geofences card background
    Then the Geofences card should have a dark blue background

  @aseed-ui @cards @geofences
  Scenario: Verify Geofences card positioning
    Then the Geofences card should be in the second row

  @aseed-ui @cards @geofences
  Scenario: Verify Geofences card text is readable
    Then the card text should have sufficient contrast

  # ========================================
  # DASHBOARD CARDS - Layout & Grid (10 tests)
  # ========================================

  @aseed-ui @cards @layout
  Scenario: Verify dashboard cards are in a grid
    Then the dashboard cards should be arranged in a grid layout

  @aseed-ui @cards @layout
  Scenario: Verify cards have equal width
    Then all dashboard cards should have equal width

  @aseed-ui @cards @layout
  Scenario: Verify cards have equal height
    Then all dashboard cards should have equal height

  @aseed-ui @cards @layout
  Scenario: Verify card spacing is consistent
    Then the spacing between cards should be uniform

  @aseed-ui @cards @layout
  Scenario: Verify cards are in multiple rows
    Then cards should be arranged in multiple rows
    And there should be 3 cards per row

  @aseed-ui @cards @layout
  Scenario: Verify grid is responsive
    When the viewport width changes
    Then the card grid should adjust responsively

  @aseed-ui @cards @layout
  Scenario: Verify all cards are visible without scrolling
    Then all main dashboard cards should be visible in viewport

  @aseed-ui @cards @layout
  Scenario: Verify card borders and shadows
    Then cards should have subtle shadows or borders

  @aseed-ui @cards @layout
  Scenario: Verify card corners are rounded
    Then all cards should have rounded corners

  @aseed-ui @cards @layout
  Scenario: Verify cards have consistent padding
    Then all cards should have equal internal padding

  # ========================================
  # DATE AND TIME DISPLAY (5 tests)
  # ========================================

  @aseed-ui @datetime
  Scenario: Verify created date format
    Then the created date should be in format "Month DD, YYYY"
    And the created date should include relative time

  @aseed-ui @datetime
  Scenario: Verify updated date format
    Then the updated date should be in format "Month DD, YYYY"
    And the updated date should include relative time

  @aseed-ui @datetime
  Scenario: Verify relative time display
    Then the created date should show "(a day ago)" or similar
    And the updated date should show "(an hour ago)" or similar

  @aseed-ui @datetime
  Scenario: Verify date labels are bold or distinct
    Then the "Created:" label should be distinguishable
    And the "Updated:" label should be distinguishable

  @aseed-ui @datetime
  Scenario: Verify dates are below tags
    Then the date information should be positioned below tags
    And dates should be left-aligned

  # ========================================
  # ACCESSIBILITY & RESPONSIVENESS (10 tests)
  # ========================================

  @aseed-ui @accessibility
  Scenario: Verify all images have alt text
    Then all images should have descriptive alt text

  @aseed-ui @accessibility
  Scenario: Verify buttons have aria labels
    Then interactive buttons should have aria-label attributes

  @aseed-ui @accessibility
  Scenario: Verify sufficient color contrast
    Then text should have sufficient contrast with background
    And it should meet WCAG standards

  @aseed-ui @accessibility
  Scenario: Verify keyboard navigation works
    When the user navigates using Tab key
    Then focusable elements should be accessible

  @aseed-ui @accessibility
  Scenario: Verify focus indicators are visible
    When elements receive focus
    Then there should be a visible focus indicator

  @aseed-ui @accessibility
  Scenario: Verify page works on mobile viewport
    When the viewport is set to mobile size
    Then all elements should be accessible and visible

  @aseed-ui @accessibility
  Scenario: Verify page works on tablet viewport
    When the viewport is set to tablet size
    Then the layout should adapt appropriately

  @aseed-ui @accessibility
  Scenario: Verify page works on desktop viewport
    When the viewport is set to desktop size
    Then all elements should have optimal layout

  @aseed-ui @accessibility
  Scenario: Verify text is scalable
    When the user increases browser font size
    Then text should scale without breaking layout

  @aseed-ui @accessibility
  Scenario: Verify no horizontal scroll on mobile
    When viewed on mobile device
    Then there should be no horizontal scrolling

  # ========================================
  # INTERACTIVE ELEMENTS (5 tests)
  # ========================================

  @aseed-ui @interactive
  Scenario: Verify all clickable elements have cursor pointer
    When the user hovers over clickable elements
    Then the cursor should change to pointer

  @aseed-ui @interactive
  Scenario: Verify disabled elements are not clickable
    Then any disabled buttons should not respond to clicks

  @aseed-ui @interactive
  Scenario: Verify tooltips on hover
    When the user hovers over icons
    Then helpful tooltips should appear

  @aseed-ui @interactive
  Scenario: Verify loading states
    When actions are processing
    Then appropriate loading indicators should appear

  @aseed-ui @interactive
  Scenario: Verify no broken links
    Then all links on the page should be valid
    And links should navigate to correct destinations

  # Total scenarios: 105+
