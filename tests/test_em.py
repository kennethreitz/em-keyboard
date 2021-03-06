from unittest.mock import call, patch

import pytest

from em import cli


@pytest.mark.parametrize(
    "test_name",
    [
        "star",
        ":star:",
    ],
)
@patch("em.docopt")
@patch("em.sys.exit")
@patch("em.xerox.copy")
@patch("builtins.print")
def test_star(mock_print, mock_xerox, mock_exit, mock_docopt, test_name):
    # Arrange
    mock_docopt.return_value = {"<name>": [test_name], "--no-copy": None, "-s": None}

    # Act
    cli()

    # Assert
    mock_xerox.assert_called_once_with("⭐")
    mock_print.assert_called_once_with("Copied! ⭐")


@patch("em.docopt")
@patch("em.sys.exit")
@patch("em.xerox.copy")
@patch("builtins.print")
def test_not_found(mock_print, mock_xerox, mock_exit, mock_docopt):
    # Arrange
    mock_docopt.return_value = {"<name>": ["xxx"], "--no-copy": None, "-s": None}

    # Act
    cli()

    # Assert
    mock_xerox.assert_not_called()
    mock_print.assert_called_once_with("")


@patch("em.docopt")
@patch("em.sys.exit")
@patch("em.xerox.copy")
@patch("builtins.print")
def test_no_copy(mock_print, mock_xerox, mock_exit, mock_docopt):
    # Arrange
    mock_docopt.return_value = {"<name>": ["star"], "--no-copy": True, "-s": None}

    # Act
    cli()

    # Assert
    mock_xerox.assert_not_called()
    mock_print.assert_called_once_with("⭐")


@patch("em.docopt")
@patch("em.sys.exit")
@patch("em.xerox.copy")
@patch("builtins.print")
def test_search_star(mock_print, mock_xerox, mock_exit, mock_docopt):
    # Arrange
    mock_docopt.return_value = {"<name>": ["star"], "--no-copy": None, "-s": True}
    expected = (
        "💫  dizzy",
        "⭐  star",
        "✳️  eight_spoked_asterisk",
    )

    # Act
    cli()

    # Assert
    mock_xerox.assert_not_called()
    for arg in expected:
        assert call(arg) in mock_print.call_args_list
