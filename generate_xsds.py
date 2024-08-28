#!/usr/bin/env python

import sys
import os
from litp.core.schemawriter import SchemaWriter


def generate_xsd_schema(root_path):
    print "\n---- Creating LITP XSD using root_path: '%s' ----\n" % (root_path)
    schema_path = os.path.join(root_path, "share", "xsd")
    print "\n---- Creating LITP XSD directory: '%s' ----\n" % (schema_path)
    os.makedirs(schema_path)
    basepaths = [os.path.join(root_path, "etc/plugins"),
                 os.path.join(root_path, "etc/extensions")]
    #print "\n---- Creating LITP XSD from: %s ----\n" % (basepaths)
    SchemaWriter(schema_path, basepaths).write()
    xsd_path = os.path.join(schema_path, "litp.xsd")
    print "\n---- LITP XSD created at: %s ----\n" % (os.path.abspath(xsd_path))

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print 'Error: Please specify the LITP root path from which to generate a LITP XSD'
        print 'usage:', sys.argv[0], '<LITP ROOT PATH>'
        sys.exit(1)
    else:
        root_path = sys.argv[1]


    print "\n---- Generating XSD files for LITP ----\n"
    generate_xsd_schema(root_path)
