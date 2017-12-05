
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Detect malicious files')

    #main method will initialize a command line parse
    #'FILE' is the target file to be classified
    parser.add_argument('FILE', help='File to be tested')
    args = parser.parse_args()

    # Load classifier (the one we trained)
    clf = joblib.load(os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'classifier/classifier.pkl'
    ))

    # Load the features
    features = pickle.loads(open(os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'classifier/features.pkl'),
        'r').read()
    )

    #extract the bytestream from our input file
    data = extract_infos(args.FILE)

    pe_features = map(lambda x:data[x], features)

    res= clf.predict([pe_features])[0]
    print('The file %s is %s' % (
        os.path.basename(sys.argv[1]),
        ['malicious', 'legitimate'][res])
    )
