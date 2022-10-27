#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the attribute container interface."""

import unittest

from plaso.containers import interface

from tests import test_lib as shared_test_lib


class TestAttributeContainer(interface.AttributeContainer):
  """Attribute container for testing purposes."""

  CONTAINER_TYPE = 'test'

  def __init__(self):
    """Initializes an attribute container."""
    super(TestAttributeContainer, self).__init__()
    self._protected_attribute = None
    self.attribute_name = None
    self.attribute_value = None


class TestAttributeContainerWithSchema(interface.AttributeContainer):
  """Attribute container for testing purposes."""

  CONTAINER_TYPE = 'test_with_schema'

  SCHEMA = {
      '_protected_attribute': 'AttributeContainerIdentifier',
      'attribute_name': 'str',
      'attribute_value': 'str'}

  _SERIALIZABLE_PROTECTED_ATTRIBUTES = ['_protected_attribute']

  def __init__(self):
    """Initializes an attribute container."""
    super(TestAttributeContainerWithSchema, self).__init__()
    self._protected_attribute = None
    self.attribute_name = None
    self.attribute_value = None


class AttributeContainerIdentifierTest(shared_test_lib.BaseTestCase):
  """Tests for the attribute container identifier."""

  def testCopyToString(self):
    """Tests the CopyToString function."""
    identifier = interface.AttributeContainerIdentifier()

    expected_identifier_string = '{0:d}'.format(id(identifier))
    identifier_string = identifier.CopyToString()
    self.assertEqual(identifier_string, expected_identifier_string)


class AttributeContainerTest(shared_test_lib.BaseTestCase):
  """Tests for the attribute container interface."""

  # pylint: disable=protected-access

  def testCopyToDict(self):
    """Tests the CopyToDict function."""
    attribute_container = TestAttributeContainer()
    attribute_container._protected_attribute = 'protected'
    attribute_container.attribute_name = 'attribute_name'
    attribute_container.attribute_value = 'attribute_value'

    expected_dict = {
        'attribute_name': 'attribute_name',
        'attribute_value': 'attribute_value'}

    test_dict = attribute_container.CopyToDict()

    self.assertEqual(test_dict, expected_dict)

  def testGetAttributeNames(self):
    """Tests the GetAttributeNames function."""
    attribute_container = TestAttributeContainer()
    attribute_container._protected_attribute = 'protected'
    attribute_container.attribute_name = 'attribute_name'
    attribute_container.attribute_value = 'attribute_value'

    expected_attribute_names = ['attribute_name', 'attribute_value']

    attribute_names = sorted(attribute_container.GetAttributeNames())

    self.assertEqual(attribute_names, expected_attribute_names)

    attribute_container = TestAttributeContainerWithSchema()
    attribute_container._protected_attribute = 'protected'
    attribute_container.attribute_name = 'attribute_name'
    attribute_container.attribute_value = 'attribute_value'

    expected_attribute_names = [
        '_protected_attribute', 'attribute_name', 'attribute_value']

    attribute_names = sorted(attribute_container.GetAttributeNames())

    self.assertEqual(attribute_names, expected_attribute_names)

  def testGetAttributes(self):
    """Tests the GetAttributes function."""
    attribute_container = TestAttributeContainer()
    attribute_container._protected_attribute = 'protected'
    attribute_container.attribute_name = 'attribute_name'
    attribute_container.attribute_value = 'attribute_value'

    expected_attributes = [
        ('attribute_name', 'attribute_name'),
        ('attribute_value', 'attribute_value')]

    attributes = sorted(attribute_container.GetAttributes())

    self.assertEqual(attributes, expected_attributes)

    attribute_container = TestAttributeContainerWithSchema()
    attribute_container._protected_attribute = 'protected'
    attribute_container.attribute_name = 'attribute_name'
    attribute_container.attribute_value = 'attribute_value'

    expected_attributes = [
        ('_protected_attribute', 'protected'),
        ('attribute_name', 'attribute_name'),
        ('attribute_value', 'attribute_value')]

    attributes = sorted(attribute_container.GetAttributes())

    self.assertEqual(attributes, expected_attributes)

  def testGetAttributeValueHash(self):
    """Tests the GetAttributeValuesHash function."""
    attribute_container = TestAttributeContainer()
    attribute_container._protected_attribute = 'protected'
    attribute_container.attribute_name = 'attribute_name'
    attribute_container.attribute_value = 'attribute_value'

    attribute_values_hash1 = attribute_container.GetAttributeValuesHash()

    attribute_container.attribute_value = 'changes'

    attribute_values_hash2 = attribute_container.GetAttributeValuesHash()

    self.assertNotEqual(attribute_values_hash1, attribute_values_hash2)

    attribute_container.attribute_value = 'attribute_value'

    attribute_container = TestAttributeContainerWithSchema()
    attribute_container._protected_attribute = 'protected'
    attribute_container.attribute_name = 'attribute_name'
    attribute_container.attribute_value = 'attribute_value'

    attribute_values_hash2 = attribute_container.GetAttributeValuesHash()

    self.assertNotEqual(attribute_values_hash1, attribute_values_hash2)

  def testGetAttributeValuesString(self):
    """Tests the GetAttributeValuesString function."""
    attribute_container = TestAttributeContainer()
    attribute_container._protected_attribute = 'protected'
    attribute_container.attribute_name = 'attribute_name'
    attribute_container.attribute_value = 'attribute_value'

    attribute_values_string1 = attribute_container.GetAttributeValuesString()

    attribute_container.attribute_value = 'changes'

    attribute_values_string2 = attribute_container.GetAttributeValuesString()

    self.assertNotEqual(attribute_values_string1, attribute_values_string2)

    attribute_container.attribute_value = 'attribute_value'

    attribute_container = TestAttributeContainerWithSchema()
    attribute_container._protected_attribute = 'protected'
    attribute_container.attribute_name = 'attribute_name'
    attribute_container.attribute_value = 'attribute_value'

    attribute_values_string2 = attribute_container.GetAttributeValuesString()

    self.assertNotEqual(attribute_values_string1, attribute_values_string2)

  def testGetIdentifier(self):
    """Tests the GetIdentifier function."""
    attribute_container = TestAttributeContainer()

    identifier = attribute_container.GetIdentifier()

    self.assertIsNotNone(identifier)

  def testMatchesExpression(self):
    """Tests the MatchesExpression function."""
    attribute_container = TestAttributeContainer()
    attribute_container.attribute_name = 'value'

    result = attribute_container.MatchesExpression('attribute_name == "value"')
    self.assertTrue(result)

    result = attribute_container.MatchesExpression('attribute_name == "bogus"')
    self.assertFalse(result)

    result = attribute_container.MatchesExpression('bogus')
    self.assertFalse(result)

  def testSetIdentifier(self):
    """Tests the SetIdentifier function."""
    attribute_container = TestAttributeContainer()

    attribute_container.SetIdentifier(None)


if __name__ == '__main__':
  unittest.main()
