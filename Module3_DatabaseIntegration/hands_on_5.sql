-- TASK 1 : Create the Collection and Insert Documents

-- 60. In MongoDB Compass or mongosh, create a database named college_nosql.
-- use college_nosql

-- 61. Create a collection named feedback.
-- db.createCollection("feedbacks")

-- 62. Insert at least 10 feedback documents following the schema above. Vary ratings (1–5), tags, and semesters. Include at least 3 documents for CS101 and 2 for CS102.
-- db.feedbacks.insertMany([ {..}, {..}, {..}, ... ] );

-- 63. Insert one document that intentionally omits the attachments field — MongoDB's schema-less design allows this.
-- db.feedbacks.insertOne({...})

-- 64. Verify the inserts using db.feedback.countDocuments().
-- db.feedbacks.countDocuments()

/* TASK 1 OUTPUT
test> use college_nosql
switched to db college_nosql
college_nosql>

college_nosql> db.createCollection("feedbacks")
{ ok: 1 }

college_nosql> db.feedback.insertMany([
  {
    student_id: 1,
    course_code: 'CS101',
    semester: '2022-ODD',
    rating: 5,
    comments: 'Excellent teaching. Highly interactive and clear explanations.',
    tags: ['well-structured', 'good-examples', 'engaging'],
    submitted_at: ISODate('2022-11-30T10:15:00Z'),
    attachments: [{ filename: 'lecture_notes_u1.pdf', size_kb: 240 }]
  },
  {
    student_id: 2,
    course_code: 'CS101',
    semester: '2022-ODD',
    rating: 4,
    comments: 'Great course content, but assignments were quite time-consuming.',
    tags: ['challenging', 'good-examples'],
    submitted_at: ISODate('2022-12-02T14:20:00Z'),
    attachments: []
  },
  {
    student_id: 3,
    course_code: 'CS101',
    semester: '2023-EVEN',
    rating: 2,
    comments: 'The pace was too fast for beginners. Difficult to follow the programming logic.',
    tags: ['fast-paced', 'heavy-workload'],
    submitted_at: ISODate('2023-05-14T09:30:00Z'),
    attachments: [{ filename: 'syllabus_feedback.docx', size_kb: 45 }]
  },
  {
    student_id: 4,
    course_code: 'CS101',
    semester: '2023-ODD',
    rating: 5,
    comments: 'Loved the hands-on lab sessions. Everything was perfectly organized.',
    tags: ['well-structured', 'practical', 'good-examples'],
    submitted_at: ISODate('2023-11-20T11:05:00Z'),
    attachments: []
  },
  {
    student_id: 5,
    course_code: 'CS102',
    semester: '2023-EVEN',
    rating: 4,
    comments: 'Solid introduction to Data Structures. The mid-term was tough.',
    tags: ['challenging', 'well-structured'],
    submitted_at: ISODate('2023-05-18T16:45:00Z'),
    attachments: [{ filename: 'assignment_1_review.pdf', size_kb: 180 }]
  },
  {
    student_id: 6,
    course_code: 'CS102',
    semester: '2023-ODD',
    rating: 1,
    comments: 'The grading criteria were very unclear and support was lacking.',
    tags: ['harsh-grading', 'poor-support'],
    submitted_at: ISODate('2023-12-01T08:00:00Z'),
    attachments: []
  },
  {
    student_id: 7,
    course_code: 'CS102',
    semester: '2024-EVEN',
    rating: 3,
    comments: 'Average course. Standard curriculum but tutorials could be improved.',
    tags: ['average-pace', 'standard-content'],
    submitted_at: ISODate('2024-05-22T13:12:00Z'),
    attachments: []
  },
  {
    student_id: 8,
    course_code: 'EE201',
    semester: '2023-ODD',
    rating: 5,
    comments: 'The professor made complex circuit analysis feel like basic math. Amazing class.',
    tags: ['engaging', 'good-examples', 'clear-explanations'],
    submitted_at: ISODate('2023-11-28T10:00:00Z'),
    attachments: [{ filename: 'lab_cheatsheet.pdf', size_kb: 512 }]
  },
  {
    student_id: 9,
    course_code: 'MA101',
    semester: '2022-ODD',
    rating: 3,
    comments: 'Calculus concepts were clear, but the exams had things not covered in class.',
    tags: ['challenging', 'heavy-workload'],
    submitted_at: ISODate('2022-11-29T15:34:00Z'),
    attachments: []
  },
  {
    student_id: 10,
    course_code: 'CS203',
    semester: '2024-ODD',
    rating: 4,
    comments: 'Great fundamentals on Operating Systems. Highly recommended for software tracks.',
    tags: ['practical', 'well-structured'],
    submitted_at: ISODate('2024-11-15T12:00:00Z'),
    attachments: [{ filename: 'os_notes.txt', size_kb: 12 }]
  }
]);
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a3acfd48c6ad0dbe0abc114'),
    '1': ObjectId('6a3acfd48c6ad0dbe0abc115'),
    '2': ObjectId('6a3acfd48c6ad0dbe0abc116'),
    '3': ObjectId('6a3acfd48c6ad0dbe0abc117'),
    '4': ObjectId('6a3acfd48c6ad0dbe0abc118'),
    '5': ObjectId('6a3acfd48c6ad0dbe0abc119'),
    '6': ObjectId('6a3acfd48c6ad0dbe0abc11a'),
    '7': ObjectId('6a3acfd48c6ad0dbe0abc11b'),
    '8': ObjectId('6a3acfd48c6ad0dbe0abc11c'),
    '9': ObjectId('6a3acfd48c6ad0dbe0abc11d')
  }
}

college_nosql> db.feedbacks.insertOne({
   student_id: 11,
   course_code: 'CS101',
   semester: '2024-ODD',
   rating: 5,
   comments: 'Brilliant course. This document deliberately skips the attachments array entirely.',
   tags: ['well-structured', 'clear-explanations'],
   submitted_at: ISODate('2024-11-18T09:45:00Z')
});
{
  acknowledged: true,
  insertedId: ObjectId('6a3ad4df8c6ad0dbe0abc11e')
}

college_nosql> db.feedbacks.countDocuments()
11
*/

-- TASK 2 : CRUD Operations

-- 65. READ: Find all feedback documents where rating is 5
-- db.feedbacks.find({ rating: 5 })

-- 66. READ: Find feedback for course CS101 where the tags array contains 'challenging'. Use $elemMatch or a simple array value query.
-- db.feedbacks.find({ course_code: 'CS101', tags: 'challenging'})

-- 67. READ: Retrieve only the student_id, course_code, and rating fields (projection) for all documents — exclude _id.
-- db.feedbacks.find({}, { student_id: 1, course_code: 1, rating: 1, _id: 0 })

-- 68. UPDATE: For all feedback documents with rating < 3, add a field needs_review: true using updateMany and $set.
-- db.feedbacks.updateMany({ rating: { $lt: 3 } }, { $set: { needs_review: true } } )

-- 69. UPDATE: Push a new tag 'reviewed' into the tags array of all documents where needs_review is true, using $push.
-- db.feedbacks.updateMany({needs_review: true}, {$push: {tags: 'reviewed'}})

-- 70. DELETE: Delete all feedback documents where the semester is '2021-EVEN'.
-- db.feedbacks.deleteMany({semester: '2021-EVEN'})

/* TASK 2 OUTPUT
college_nosql> db.feedbacks.find({rating: 5})
[
  {
    _id: ObjectId('6a3acfd48c6ad0dbe0abc114'),
    student_id: 1,
    course_code: 'CS101',
    semester: '2022-ODD',
    rating: 5,
    comments: 'Excellent teaching. Highly interactive and clear explanations.',
    tags: [ 'well-structured', 'good-examples', 'engaging' ],
    submitted_at: ISODate('2022-11-30T10:15:00.000Z'),
    attachments: [ { filename: 'lecture_notes_u1.pdf', size_kb: 240 } ]
  },
  {
    _id: ObjectId('6a3acfd48c6ad0dbe0abc117'),
    student_id: 4,
    course_code: 'CS101',
    semester: '2023-ODD',
    rating: 5,
    comments: 'Loved the hands-on lab sessions. Everything was perfectly organized.',
    tags: [ 'well-structured', 'practical', 'good-examples' ],
    submitted_at: ISODate('2023-11-20T11:05:00.000Z'),
    attachments: []
  },
  {
    _id: ObjectId('6a3acfd48c6ad0dbe0abc11b'),
    student_id: 8,
    course_code: 'EE201',
    semester: '2023-ODD',
    rating: 5,
    comments: 'The professor made complex circuit analysis feel like basic math. Amazing class.',
    tags: [ 'engaging', 'good-examples', 'clear-explanations' ],
    submitted_at: ISODate('2023-11-28T10:00:00.000Z'),
    attachments: [ { filename: 'lab_cheatsheet.pdf', size_kb: 512 } ]
  },
  {
    _id: ObjectId('6a3ad4df8c6ad0dbe0abc11e'),
    student_id: 11,
    course_code: 'CS101',
    semester: '2024-ODD',
    rating: 5,
    comments: 'Brilliant course. This document deliberately skips the attachments array entirely.',
    tags: [ 'well-structured', 'clear-explanations' ],
    submitted_at: ISODate('2024-11-18T09:45:00.000Z')
  }
]

college_nosql> db.feedbacks.find({course_code: 'CS101', tags: 'challenging'})
[
  {
    _id: ObjectId('6a3acfd48c6ad0dbe0abc115'),
    student_id: 2,
    course_code: 'CS101',
    semester: '2022-ODD',
    rating: 4,
    comments: 'Great course content, but assignments were quite time-consuming.',
    tags: [ 'challenging', 'good-examples' ],
    submitted_at: ISODate('2022-12-02T14:20:00.000Z'),
    attachments: []
  }
]

college_nosql> db.feedbacks.find({}, {student_id: 1, course_code: 1, rating: 1, _id: 0})
[
  { student_id: 1, course_code: 'CS101', rating: 5 },
  { student_id: 2, course_code: 'CS101', rating: 4 },
  { student_id: 3, course_code: 'CS101', rating: 2 },
  { student_id: 4, course_code: 'CS101', rating: 5 },
  { student_id: 5, course_code: 'CS102', rating: 4 },
  { student_id: 6, course_code: 'CS102', rating: 1 },
  { student_id: 7, course_code: 'CS102', rating: 3 },
  { student_id: 8, course_code: 'EE201', rating: 5 },
  { student_id: 9, course_code: 'MA101', rating: 3 },
  { student_id: 10, course_code: 'CS203', rating: 4 },
  { student_id: 11, course_code: 'CS101', rating: 5 }
]

college_nosql> db.feedbacks.updateMany({rating: {$lt: 3}}, {$set: {needs_review: true}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 2,
  modifiedCount: 2,
  upsertedCount: 0
}

college_nosql> db.feedbacks.updateMany({needs_review: true}, {$push: {tags: 'reviewed'}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 2,
  modifiedCount: 2,
  upsertedCount: 0
}

college_nosql> db.feedbacks.deleteMany({semester: '2021-EVEN'})
{ acknowledged: true, deletedCount: 0 }

*/

-- TASK 3 : Aggregation Pipeline

-- 71. Write a pipeline that: (Stage 1) filters to semester '2022-ODD'; (Stage 2) groups by course_code calculating average rating and total feedback count; (Stage 3) sorts by average rating descending.

-- 72. Extend the pipeline with a $project stage to rename avg_rating to average_rating and round it to 1 decimal place using $round.

-- 73. Write a pipeline that uses $unwind on the tags array, then $group by tag to count how many times each tag appears. Sort by count descending — a tag frequency leaderboard.

-- 74. Add an index on course_code and verify its usage with db.feedback.find({course_code:'CS101'}).explain('executionStats') — confirm the stage shows IXSCAN not COLLSCAN.

/* TASK 3 OUTPUT
college_nosql> const pipeline = [
    { $match: { semester: '2022-ODD' } },
    { $group: {
        _id: "$course_code",
        avg_rating: { $avg: "$rating" },
        total_feedback: { $sum: 1 }
        } 
    },
    { $sort: { avg_rating: -1 } }
];

college_nosql> db.feedbacks.aggregate(pipeline)
[
  { _id: 'CS101', avg_rating: 4.5, total_feedback: 2 },
  { _id: 'MA101', avg_rating: 3, total_feedback: 1 }
]

college_nosql> pipeline.push({
    $project: {
        _id: 0,
        course_code: "$_id",
        total_feedback: 1,
        average_rating: { $round: ["$avg_rating", 1] }
    }
});
4
college_nosql> db.feedbacks.aggregate(pipeline)
[
  { total_feedback: 2, course_code: 'CS101', average_rating: 4.5 },
  { total_feedback: 1, course_code: 'MA101', average_rating: 3 }
]

college_nosql> db.feedbacks.aggregate([
  { 
    $unwind: "$tags" 
  },

  { 
    $group: {
      _id: "$tags",
      count: { $sum: 1 }
    } 
  },

  { 
    $sort: { count: -1 } 
  }
]);
[
  { _id: 'well-structured', count: 5 },
  { _id: 'good-examples', count: 4 },
  { _id: 'challenging', count: 3 },
  { _id: 'engaging', count: 2 },
  { _id: 'heavy-workload', count: 2 },
  { _id: 'reviewed', count: 2 },
  { _id: 'clear-explanations', count: 2 },
  { _id: 'practical', count: 2 },
  { _id: 'average-pace', count: 1 },
  { _id: 'fast-paced', count: 1 },
  { _id: 'poor-support', count: 1 },
  { _id: 'standard-content', count: 1 },
  { _id: 'harsh-grading', count: 1 }
]

college_nosql> db.feedbacks.createIndex({ courcourse_code: 1 })
course_code_1
college_nosql> db.feedbacks.find({course_code: 'CS101' }).explain('executionStats')
{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'college_nosql.feedbacks',
    parsedQuery: { course_code: { '$eq': 'CS101' } },
    indexFilterSet: false,
    queryHash: '83CE04A5',
    planCacheShapeHash: '83CE04A5',
    planCacheKey: 'E4E1D11D',
    optimizationTimeMillis: 11,
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    prunedSimilarIndexes: false,
    winningPlan: {
      isCached: false,
      stage: 'FETCH',
      nss: 'college_nosql.feedbacks',
      inputStage: {
        stage: 'IXSCAN',
        nss: 'college_nosql.feedbacks',
        keyPattern: { course_code: 1 },
        indexName: 'course_code_1',
        isMultiKey: false,
        multiKeyPaths: { course_code: [] },
        isUnique: false,
        isSparse: false,
        isPartial: false,
        indexVersion: 2,
        direction: 'forward',
        indexBounds: { course_code: [ '["CS101", "CS101"]' ] }
      }
    },
    rejectedPlans: []
  },
  executionStats: {
    executionSuccess: true,
    nReturned: 5,
    executionTimeMillis: 97,
    totalKeysExamined: 5,
    totalDocsExamined: 5,
    executionStages: {
      isCached: false,
      stage: 'FETCH',
      nReturned: 5,
      executionTimeMillisEstimate: 39,
      works: 6,
      advanced: 5,
      needTime: 0,
      needYield: 0,
      saveState: 1,
      restoreState: 1,
      isEOF: 1,
      nss: 'college_nosql.feedbacks',
      docsExamined: 5,
      alreadyHasObj: 0,
      inputStage: {
        stage: 'IXSCAN',
        nReturned: 5,
        executionTimeMillisEstimate: 39,
        works: 6,
        advanced: 5,
        needTime: 0,
        needYield: 0,
        saveState: 1,
        restoreState: 1,
        isEOF: 1,
        nss: 'college_nosql.feedbacks',
        keyPattern: { course_code: 1 },
        indexName: 'course_code_1',
        isMultiKey: false,
        multiKeyPaths: { course_code: [] },
        isUnique: false,
        isSparse: false,
        isPartial: false,
        indexVersion: 2,
        direction: 'forward',
        indexBounds: { course_code: [ '["CS101", "CS101"]' ] },
        keysExamined: 5,
        seeks: 1,
        dupsTested: 0,
        dupsDropped: 0,
        peakTrackedMemBytes: 0
      }
    }
  },
  queryShapeHash: 'E34073303E4EF51C6564FCF3835D0691122035590857659A68C7878951175498',
  command: {
    find: 'feedbacks',
    filter: { course_code: 'CS101' },
    '$db': 'college_nosql'
  },
  serverInfo: {
    host: 'DESKTOP-S39TI2U',
    port: 27017,
    version: '8.3.4',
    gitVersion: '4b03e7daaa316c78b9bf433046dba81637d581c0'
  },
  serverParameters: {
    internalQueryFacetBufferSizeBytes: 104857600,
    internalDocumentSourceGroupMaxMemoryBytes: 104857600,
    internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
    internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600,
    internalQueryFacetMaxOutputDocSizeBytes: 104857600,
    internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
    internalQueryProhibitBlockingMergeOnMongoS: 0,
    internalQueryMaxAddToSetBytes: 104857600,
    internalQueryFrameworkControl: 'trySbeRestricted',
    internalQueryPlannerIgnoreIndexWithCollationForRegex: 1
  },
  ok: 1
}
*/